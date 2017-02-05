'''
using this little script to encode some plain text and send them to your friend
and let them decode it themselves!

'''

import base64
import os 
import string

def build_and_write():
	try:
		true_or_false = os.path.isfile('flag.txt')
		another = os.path.isfile('encrypted.txt')

		#first time using the program
		if true_or_false==False and another==False:
			print 'file \'flag.txt\' does not exist! building now...\n'
			f = open('flag.txt','w')
			f.write('0')
			f.close()
		#get encrypted text from friend,don't have flag file
		elif true_or_false==False and another == True:
			f = open('flag.txt','w')
			f.write('1')
			f.close()

		elif true_or_false==True and os.path.getsize('flag.txt')==False:
			print 'file exist but empty.Writing defalut value 0 to it...\n'
			f = open('flag.txt','w')
			f.write('0')
			f.close()
	except:
		print 'something fail!'

def input_data():
	print 'if you are going to enter a paragraph,choose(1),else choose(0)'
	choose = (int)(raw_input("0/1\n"))
	if choose == 1:
		data_set = []
		print "enter lines:"
		lines = (int)(raw_input('lines:')) + 1
		for item in range(1,lines):
			data = raw_input('data:>>>\n')
			data_set.append(data)
		return '\n'.join(data_set)
	elif choose == 0:
		data = raw_input('data:>>>\n')
		return data


def encrypted_or_decoded():
	if flag==0:
		f = open('encrypted.txt','w')
		f1 = open('flag.txt','w')
		data = input_data()
		f.write(base64.b64encode(data))
		f1.write('1')

		f.close()
		f1.close()
		print 'Data encrypted success!'
	
	
	elif flag ==1:
		print 'Decoding to decoded.txt....\n'
		f = open('decoded.txt','w')
		f2 = open('encrypted.txt','r')
		f1 = open('flag.txt','w')
		data = f2.read()
		data = base64.b64decode(data)
		f.write(data)

		f1.write('0')

		f.close()
		f2.close()
		f1.close()
		print 'Decode success!'


if __name__ == '__main__':
	build_and_write()
	f1 = open('flag.txt','r')
	flag=(int)(f1.read())
	print 'now flag is : %d' %flag
	f1.close()
	encrypted_or_decoded()
	
	

	

