# -*- coding: utf-8 -*-
'''
a script that need pillow ,pytesseract and tesseract-ocr to recognize chinese chracter image
'''
from PIL import Image  
import pytesseract  
#只对很纯的中文文本截图有效
text=pytesseract.image_to_string(Image.open('tt.png'),lang='chi_sim') #设置为中文文字的识别
# text=pytesseract.image_to_string(Image.open('tt.jpg'),lang='eng')   #设置为英文或阿拉伯字母的识别
file = open("imageinfo.txt",'w',encoding="utf8")
file.write(text)
file.close()
print("file write success!")