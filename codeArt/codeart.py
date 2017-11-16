from pyfiglet import Figlet
import os



def inputAndTransform():
    dirPath =  os.curdir
    write = input("What do you want to write? Please input here:\n")
    f = Figlet(font='ogre') # 斜体 不slant是默认的字体 是不倾斜的
    textWrite = "```\n"+f.renderText(write)+"\n```"
    with open("codepic.txt", "w") as f:
        f.writelines(textWrite)


if __name__ == '__main__':
    inputAndTransform()
    print ("Write success!")

