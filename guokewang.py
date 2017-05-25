__author__ = 'wendy'

import requests
from bs4 import BeautifulSoup
import os


class GUOKE:

    def __init__(self,baseURL,id=""):
        self.url = baseURL + str('/'+id+'/')
        self.contents= []
        self.floor = 1
        self.defaultTitle = "guoke"
        self.fileTitle = ""
        self.file = None


    def getInfo(self):
        url = self.url
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36','Content-Type':'text/html'}
        res = requests.get(url,headers=headers)
        res.encoding='utf-8'
        soup = BeautifulSoup(res.text,'html.parser')

        floor = 0
        answernumstring = soup.select('.answers-do span')[0]['content']
        answernum = int(answernumstring.encode("utf-8"))
        try:
            title = soup.select('#articleTitle')[0].text
            print('-------------------------title: '+ title)
        except UnicodeEncodeError as e:
            print('--------------------------title has emoji!')
            title = "page title illegal"


        
        #store one page
        floorcontents = []

        while floor < answernum:
            name = soup.select('.answer-usr-name')[floor].text
            
            answer = soup.select('.answer-txt')[floor].text
            date = soup.select('.answer-date')[floor].text
            
           

            print('answer-usr-name: '+name+'\t\t'+'date: '+date)       
            print('answer: '+answer)
            print(u'-----------------------------------------------------------')
            floor+=1 


            floorcontents.append(name)
            floorcontents.append(date)
            floorcontents.append(answer)

            self.contents.append(floorcontents)
            floorcontents = []
            if floor >20:
                break;

        return title

       
    #set file title
    def setFileTitle(self,fileTitle):
        if fileTitle==self.defaultTitle:
            self.file = open(self.defaultTitle + ".txt","w+")
        else:
            self.fileTitle = fileTitle
            self.file = open(self.fileTitle + ".txt","w+")
    
    #write data to one file
    def writeData(self,title):

        self.file.write("title: "+ title +'\n')
        for item in self.contents:         
            floorLine = "\n" + str(self.floor) + u"-------------------------------------------------------------\n"
            self.file.write(floorLine)
            self.file.write(item[0]+'\t')
            self.file.write(item[1]+'\n')
            self.file.write(item[2]+'\n')
            self.floor += 1
        print('file save success!!\n')
        # stop = input("hit enter to continue...\n")


    #get this page's question id
    def getQAID(self):
        url = 'http://www.guokr.com/ask/'
        res = requests.get(url)
        res.encoding='utf-8'
        soup = BeautifulSoup(res.text,'html.parser')

        counter=0
        IDList=[]
        #this page only have 20 elements
        #what if doesn't?
        jcounter = 20
        while jcounter>0:
            IDhref = soup.find_all(class_= 'gellipsis')[counter]['href']
            IDsplit = IDhref.split('/')
            ID = IDsplit[4]
            IDList.append(ID)
            counter+=1
            jcounter-=1
    
        print("ALL ID:\n",IDList)
        return IDList
    
    #make folder
    def makeDir(self):
        folder="GUOKE"
        os.mkdir(folder)
        os.chdir(folder)


    #single query mode or full query mode
    def start(self,baseURL,mode):

        self.makeDir()

        if mode ==1:
            IDList = self.getQAID()
            max = 20
            counter = 0
            for item in IDList:
                self.__init__(baseURL,IDList[counter])    
                pageTitle = self.getInfo()
                fileTitle = "question" + str(counter+1)
                self.setFileTitle(fileTitle)
                self.writeData(pageTitle)
                counter+=1
            print('All file save success!')
        elif mode ==0:
            pageTitle = self.getInfo()
            self.setFileTitle(self.defaultTitle)
            self.writeData(pageTitle)


if __name__ == '__main__':
    baseURL = 'http://www.guokr.com/question/'
    mode = int(input("Enter 0 for ordinary query id else 1 for all query:\n"))
    if mode == 0:
        questionID = input("Enter question id: ")
        guoke = GUOKE(baseURL,questionID)
        guoke.start(baseURL,mode)
    elif mode==1:
        guoke = GUOKE(baseURL)
        guoke.start(baseURL,mode)


