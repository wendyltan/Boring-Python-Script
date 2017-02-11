#!/usr/bin/python  
# -*- coding: utf-8 -*-  


'''
author:wendyltanpcy
status:still-improving

'''
import itchat,time,locale
from itchat.content import *
import sys

flag = 0
me = ' '
friend_chatting = ' '

reload(sys)      
sys.setdefaultencoding('utf-8')

#uncommment it when u want to send many wishes
'''
def send_wishes():
	SINCERE_WISH = u'祝%s元宵快乐ww！'

	friendList = itchat.get_friends(update=True)[1:]
	for friend in friendList:
		# 如果是演示目的，把下面的方法改为print即可
		itchat.send(SINCERE_WISH % (friend['DisplayName']or friend['NickName']), friend['UserName'])
    	time.sleep(.5)
'''
#init your choose to chat yourself or auto reply
def choose_check():

	global flag
	choose = raw_input('got message!want to chat yourself?(y/n)')
	flag = 1
	return choose

#for group chat text reply
@itchat.msg_register([TEXT],isGroupChat=True)
def group_action(msg):
	if msg['isAt']:
		print('U are @ting by %s, saying %s '%(msg['ActualNickName'],msg['Content']))
		itchat.send(u'多谢@我！等下回复你~ %s' % msg['ActualNickName'],toUserName=msg['ActualNickName'])
	elif msg['Type'] == TEXT:
		try:
			print('G# %s is saying %s '%(msg['ActualNickName'],msg['Content']))
		except UnicodeEncodeError:
			print 'G# Receiving unaceptable image format.'
		
# for private chat text reply
@itchat.msg_register(TEXT,isFriendChat=True)
def private_reply(msg):

	global flag
	global choose
	global friend_chatting
	global me
	
	if flag==0:
		choose = choose_check() #init your choose.can not change once it start the mode

	friendList = itchat.get_friends(update=True)[1:] #get all your friends
	for friend in friendList:
		if friend['UserName'] == msg['FromUserName']:
			if friend['NickName'] == 'Wendy':#change this to your nickname on wechat.
				me = friend['UserName']
				break #save the key,use to do judgement(in order not to speak to myself)
			hint = 'match!' + (friend['NickName']) + (" is chating with u!")
			friend_chatting = friend['NickName']#current chatting with
			print '`'*len(hint)
			print hint
			print '`'*len(hint)
			
	if msg['FromUserName']!=me:
		print friend_chatting,"says: ",msg['Content']
		if choose == 'n' and flag==1:
			itchat.send('come back later,I\'m busy right now.',toUserName = msg['FromUserName'])
			print 'have send autoreply.'


		elif choose=='y' and flag==1:
			text = raw_input( ">>>enter your message:(use enter to jump reply\n" ).decode(sys.stdin.encoding or locale.getpreferredencoding(True))

			text.decode('utf-8')
			if not text=='\n':#three space enter in.
				itchat.send(text,toUserName=msg['FromUserName'])
				print 'reply have sent.'

	elif msg['FromUserName']==me: #in this circumstance,i chat on the phone at the same time.so no reply needed.
		print 'I do some talking on other client.',msg['Text']

#for private chat media object action
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO],isFriendChat=True)
def Media_reply(msg):
	if msg['Type']==PICTURE and msg['FromUserName']!=me:#if not from me,download and send specific image back
		print 'receive an image,download and replying...'
		msg['Text'](msg['FileName'])
		print 'download success!'
			#return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
			#this line use to return just the same thing other send u
		itchat.send('@img@%s' % '1.png',toUserName = msg['FromUserName'])
		print 'have send specific image back.'
	elif msg['Type']==PICTURE and msg['FromUserName']==me:
		print 'receiving image from myself.'

	elif msg['Type'] ==VIDEO and msg['FromUserName']!=me:
		itchat.send(u'哎~真还有趣',toUserName=msg['FromUserName'])
		print 'auto reply done.'

#beginning of the script.decided whether to use robot
use_robot = raw_input('use robot?(y/n)')
if use_robot=='y':
	print 'using robot...'
	execfile('robot\main.py')
	
else:
	print 'not using any robot.'
	itchat.auto_login(hotReload=True)
	'''
	send_wishe = raw_input('send wishes?(y/n)')
	if send_wishe=='y':
		send_wishes()
	'''
	itchat.run()
	itchat.dump_login_status()







