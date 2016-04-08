import os
import shutil
import string
"""print out a chart for user """
print '\t','*'*10,"copyright@WENDYLTANPCY",'*'*17
print '\t','*'*5,"The program is a simple database",'*'*12
print '\t','*'*5,"for storing small amount of information",'*'*5
print '\t\t','-'*30
print '\t\t','|',"1.   	  log in"				,'	     |'
print '\t\t','|',"2.   	  check data"			,'  	     |'
print '\t\t','|',"3.   	  change data"		,' 	     |'
print '\t\t','|',"4.   	  exit"				,'	     	     |'
print '\t\t','-'*30

"""building main function"""
__metaclass__ = type

class database(object):
	
	
	"""password confirm and user build(text.txt)"""
	def print_name(self):
		name = raw_input("please enter your name\n")
		print "So your name is : %s\n" % name
		answer = raw_input("do you already have password?(y/n)\n")
		if answer is 'n':
			file = open('text.txt','r')
			counter = 0
			if counter == 0:
				name = file.readlines()
				counter = counter+1
			else:
				name = file.readlines()[0]
			file.close()
			if name != []:
				print "the user now is %s\ndo you want to delete this user?(y/n)" % name[0]
				answer = raw_input(">")
				if answer is 'y':
					file = open('text.txt','r+')
					password = raw_input("please enter old password:\n")
					default_pass = file.readlines()[1]
					if password == default_pass:
						file.truncate(0)
						print "successfully delete the old data!\n"
						file.close()
						name = raw_input("please enter your name again\n")
						default_pass = raw_input("please enter new password\n")
						file = open('text.txt','r+')
						info = [name,'\n',default_pass]
						file.writelines(info)
						file.close()
						print "building password complete...\n"
						print "please log in.\n"
						self.print_name()
					else:
						print "error!try again!"
						file.close()
						self.print_name()
				if answer is 'n':
					pass	
			else:
				print "i guess there is no user of database!"
				name = raw_input("please enter user's name \n")
				default_pass = raw_input("please enter the password\n")
				file = open('text.txt','a+')
				info = [name,'\n',default_pass]
				file.writelines(info)
				file.close()
				print "please log in"
				self.print_name()
		elif answer is 'y':
			file = open('text.txt','r')
			password = raw_input("please enter your password :\n")
			default_pass = file.readlines()[1]
			file.close()
			if password != default_pass:
				print "error!try again\n"
				self.print_name()
			if password == default_pass:
				print "confirming...succeed!\n"
			if name is None:
				print "i guess there is no user of database!\n"
				return 0
		else:
			print "please follow the rule!\n"
			exit(0)
	

	"""check if there is already data"""
	def check_data(self):
		print "let's check the data"
		file = open('data.txt','r')
		lines = file.readlines()
		if len(lines) != 0:
			for eachline in lines:
				print eachline 
			file.close()
		if len(lines) == 0:
			print "doesn't have any data here?"
			answer = raw_input("input now?(y/n)")
			if answer is 'y':
				return 'a'
			if answer is 'n':
				return 'b'
			file.close()


	"""use this to change data"""
	def change_data(self):
		answer = raw_input("do you want to add or delete data?'q' for quit.(a/d/q)\n")
		if answer is 'a':
			file = open('data.txt','a+')
			count = 0
			alllines = file.readlines()
			for eachline in alllines:
				count +=1
			file.close()
			counter = 0
			while counter == 0:
				b_list = []
				i = 0
				if count > 0:
					b_list.append('\n')
				b_list.append(">  ")
				while i<3:
					b_list.append(raw_input("enter the name,age,phonenumber:\n"))
					if i < 2:
						b_list.append('\t') 
					counter = 1
					i+=1
				file = open('data.txt','a+')
				file.writelines(b_list)
				file.close()
				print "data write complete...\n"
				print "let's display the data:\n"
				file = open('data.txt','r')
				alllines = file.readlines()
				for eachline in alllines:
					print eachline 
				answer = raw_input("do you want to exit?(y/n)\n")
				if answer is 'y':
					return 0
				if answer is 'n':
					counter = 0
					count += 1
		
		elif answer is 'd':
			file = open('data.txt','a+')
			if file != None:
				answer = raw_input("which line of data do you want to delete?('1' for exp)\n")
				lines = open('data.txt').readlines()
				del lines[int(answer)-1]
				open("data.txt","w").writelines(lines)
				print "delete complete!"
				file.close()

	
		elif answer is 'q':
			return 0


	"""try build list of info and store it(data.txt)"""
	def build_list(self):
		print "Let's build a new list:"
		counter = 0
		count = 0
		while counter == 0:
			b_list = []
			i = 0
			if count > 0:
				b_list.append('\n')
			b_list.append(">  ")
			while i<3:
				b_list.append(raw_input("enter the name,age,phonenumber:\n"))
				if i < 2:
					b_list.append('\t') 
				counter = 1
				i+=1
			file = open('data.txt','a+')
			file.writelines(b_list)
			file.close()
			print "data write complete...\n"
			print "let's display the data:\n"
			file = open('data.txt','r')
			alllines = file.readlines()
			for eachline in alllines:
				print eachline 
			answer = raw_input("do you want to exit?(y/n)\n")
			if answer is 'y':
				return 0
			if answer is 'n':
				counter = 0
				count += 1

	#def build_dic(thelist):
		#dic = {}.fromkeys(['name','age','phonenumber'])
		#dic['name'] = thelist[0]
		#dic['age'] = thelist[1]
		#dic['phonenumber'] = thelist[2]
		#print dic

select = raw_input("please choose your option:(1/2/3/4)")
mydata = database()
if select != '1':
	print "please log in first!"
	mydata.print_name()
else:
	mydata.print_name()

while select != '4':
	select = raw_input("please choose your option:(2/3/4)")
	if select is '2':
		confirm = mydata.check_data()
		if confirm is 'a':
			mydata.build_list()
		if confirm is 'b':
			pass
	if select is '3':
		mydata.change_data()
	if select is '4':
		break

print "thanks for using the program!"



  





