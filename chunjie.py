# -*- coding: utf-8 -*-

def hongbao_get(hongbao):
    print (u"你获得的红包数量是 %s.") % hongbao
def hongbao_left(get, turnin):
    print (u"你剩余的红包数量是 %s - %s ") % (get, turnin)
    return int(get) - int(turnin)
def money_left(a, b):
    return a - b


print (u"猴年新春创意小程序")
tishi = '>> '
raw_input(tishi)

print (u"我们会以此程序计算下新春前后你获得的钱财总数。")
raw_input(tishi)

print (u"""今年是猴年，你一定从亲戚那儿获得了不少红包吧？\n你可以告诉我得了多少个红包吗""")
hongbao = raw_input("hongbao you get:")
hongbao_get(hongbao)
print (u"但是你肯定被收走了一部分红包吧？被收走了多少个呢？")
turnin = raw_input("turn in:")
hongbao_left(hongbao, turnin)
print (u"真可怜。。那么剩余的红包中你一共获得了多少钱？")
money = raw_input("the money you get:")
moneyget = int(money)
 

print (u"""所以你得到了 %d 元，这么多钱可以用来旅行哟。\n如果我说你可以去下面其中一个地方旅游，你会选哪里呢？""") % moneyget
places = ['Beijing','Shanghai','Xinrimuli','Erciyuan']
print places
choice = raw_input("places:")
if choice in places[0]:
    print (u"你可能需要3000元才能到那里")
    moneyspend = 3000
    
else :
    if choice in places[1]:
        print (u"你可能需要2500元才能到那里")
        moneyspend = 2500
        
    else :
        if choice in places[2]:
            print (u"你可能需要几名兄贵才能到那里")
            moneyspend = 0
            
        else :
                if choice in places[3]:
                    print (u"你不可能到那里")
                    moneyspend = 0
                   

print (u"旅行之后你还剩下多少钱呢？")
moneyleft = money_left(moneyget,moneyspend)
print (u"还不错，看来你还有 %d yuan.\n我们为何不趁现在给大家写一些祝福的话呢？") % moneyleft
print (u"让我们先打开这个文档。")
filename = raw_input("filename:")



wish = open(filename,'w')

print (u"我们先清空它。")
wish.truncate()

print (u"然后，我们写一些祝福")
wish_write_one = raw_input("line1:")
wish_write_two = raw_input("line2:")
wish_write_three = raw_input("line3:")
print (u"我将会把这些写入文件中。")

wish.write(wish_write_one)
wish.write("\n")
wish.write(wish_write_two)
wish.write("\n")
wish.write(wish_write_three)
wish.write("\n")
wish.close()


print (u"让我们确认一下这个文件，请再输入一次文件名。")
in_file = open(raw_input("filename:"))
wishes = in_file.read()

print "---------------------------"
print wishes
print "---------------------------"

in_file.close()


print (u"所以都完成了！HAPPY NEW YEAR!")
raw_input("hit return to quit the program>>")






