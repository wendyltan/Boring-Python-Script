#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 10:05
# @Author  : Wendyltanpcy
# @File    : text2sound.py
# @Software: PyCharm

import os
from eyed3.compat import unicode
from eyed3.id3 import ID3_V2_4
from gtts import gTTS
import eyed3
from eyed3.id3.tag import Tag
from progress.bar import Bar

class gtts_extends(gTTS):
    """
    simply extends gTTS
    """
    def __init__(self,text,lang = 'en'):
        super(gtts_extends, self).__init__(text=text,lang=lang)

    def sequence_save(self,savefile):
        """
        make it capable to append line into different language of gtts obj
        :param savefile:
        :return:
        """
        with open(savefile, 'ab') as f:
            self.write_to_fp(f)

def is_chinese(uchar):
    """
    recognize Chinese characters
    :param uchar:
    :return:
    """
    if '\u4e00' <= uchar<='\u9fff':
        return True
    else:
        return False

def is_alphabet(uchar):
    """
    recognize English characters
    :param uchar:
    :return:
    """
    if ('\u0041' <= uchar<='\u005a') or ('\u0061' <= uchar<='\u007a'):
        return True
    else:
        return False

def read_and_gen(lyric_path,file_path):
    """
    read file and generate mp3 sound file
    :param file_path:
    :return:
    """

    #remove original before adding new content in it
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(lyric_path, encoding="utf-8") as file:
        file = file.readlines()
    bar = Bar('Processing', max=file.__len__())
    for line in file:
        if is_alphabet(line[0]):
            #line should be spoken in en
            speak = gtts_extends(line,lang='en')
            speak.sequence_save(file_path)

        if is_chinese((line[0])):
            speak = gtts_extends(line, lang='zh')
            speak.sequence_save(file_path)
        bar.next()
    bar.finish()
    print("transform success!")

def set_mp3_tag(mp3_path,lyric_path):
    """
    set mp3 tag info here
    :param mp3_path:
    :param lyric_path:
    :return:
    """
    f = open(lyric_path, 'r', encoding='utf-8')
    result = u""
    for line in f.readlines():
        result += line
    audiofile = eyed3.load(mp3_path)
    t = Tag()
    # basic info
    t.title = u"B with U"
    t.artist = u"群星"
    t.album = u"2018拜年祭"
    t.genre = u"Hip-Hop"
    t.track_num = (3, 5)
    t.disc_num = (1, 1)

    # date info
    t.original_release_date = "1994-04-07"
    t.release_date = "1994-04-07"
    t.encoding_date = "2002-03"
    t.recording_date = 1996
    t.tagging_date = "2012-2-5"

    # comments
    t.comments.set(u"Gritty, yo!")
    t.comments.set(u"Brownsville, Brooklyn", u"Origin")

    t.lyrics.set(unicode(result), "b_with_u")

    audiofile.tag = t
    audiofile.tag.save(version=ID3_V2_4)

if __name__ == '__main__':
    try:
        lyric_path = input("Enter lyric file path!\n")
        file_path = input("Enter generate mp3 path and name\n")
        if not file_path.endswith('.mp3'):
            print('Invalid filename!make sure to end with .mp3')
        else:
            read_and_gen(lyric_path,file_path)
            set_mp3_tag(file_path,lyric_path)
    except FileNotFoundError:
        print("Wrong file path!")
    except IndexError:
        print("Index error!make sure to enter the right index!")





