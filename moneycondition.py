# -*- coding: utf-8 -*-
#目的：制作一个能够对现在生活有所帮助的小程序
#收支计算，下月需生活费计算小程序
#归类为：日常吃饭费用，出去浪的费用，家教收入，淘宝买东西支出，宿舍公用支出
#功能：计算平均每天花费的金额以及下个月估计花费金额以及本月所花总金额。


#writing the program to control my money use



def money_spending(dic):
	MON_USE = 0
	for key in dic:
		MON_USE += int(dic[key])
	return MON_USE

		
def money_average(cond):
	average = (cond)/31
	print "money use every day is average: %d" % average
	return average
def money_need(total):
	if total<= 1100:
		print "money use next month should be:%d\n" % ((money_average + 5)*31)
	elif total>1100:
		print "you are using too much money!try controling yourself!\n"
		print "next month needed:%d\n" % ((money_average -3)*31)




print "please enter the money you have use for this month one after another :\n"	

money_condition_list = ["money_eat","money_hangout","money_netshop","money_dorm"]	
money_condition  = {}

for con in money_condition_list:
	print con
	money_condition[con] = raw_input("enter the money that this condition needed:\n")
print money_condition



money_get = raw_input("money get from tutoring:")
money_spend = money_spending(money_condition)
print "the money you spend is totally :%d" % money_spend
money_total = int(money_spend) - int(money_get)
money_average = money_average(money_total)

money_need = money_need(money_total)




