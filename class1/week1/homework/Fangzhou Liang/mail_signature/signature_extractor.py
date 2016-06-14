# -*- coding:utf-8 -*-
import sys
import re
import jieba.posseg as pseg
import nltk

if len(sys.argv) < 2:
    print 'No Files!'
    sys.exit(1)
else:
    file_list = sys.argv[1:]

name_reg = re.compile( ur'''
                        ^
                        \ *((姓名|Name|name){1}(:|-|：|\ )*)?
                        (([\u4e00-\u9fa5]{2,4}(?!\·))|([\u4e00-\u9fa5]{2,4}(\·{1}[\u4e00-\u9fa5]{1,4}){1,4}))?
                        \ *
                        ([a-zA-Z\ ,]{1,20})?
                        \ *
                        $
                        ''', re.X )  # get group 3 7 index-0
phone_reg = re.compile(ur'''
                        ^
                        ((Tel|电话|手机|Mobile){1}(:|-|：|\ )*)?
                        ((?<![-_.@a-zA-Z])(\+?[0-9\ \-]{8,})(?![-_.@a-zA-Z]))
                        ''', re.X)  # get group 3 index-0
mail_reg = re.compile( ur'''
                        ((((e-)?mail|(e|E-)?MAIL|(e|E-)?Mail)|邮箱){1}(:|-|：|\ )*)?
                        (([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5}){1,25})
                        ''', re.X)  # get group 7 index-0

for each_file in file_list:
    f = open(each_file, 'r')
    lines = f.readlines()
    name_tuple = name_reg.findall(lines[0].decode('utf-8'))[0]
    name = [name_tuple[3], name_tuple[7]]
    phone_num = []
    email = []
    org = []
    for each_line in lines[1:]:
        # parse phone number
        phone = phone_reg.findall(each_line.decode('utf-8'))
        if phone != []:
            phone_num.append(phone[0][3])
            each_line = phone_reg.sub('', each_line)
        # parse e-mail address
        mail = mail_reg.findall(each_line.decode('utf-8'))
        if mail != []:
            email.append(mail[0][7])
            each_line = mail_reg.sub('', each_line)
        # parse organization
        jieba_noun = [each_word.word for each_word in pseg.cut(
            each_line) if each_word.flag in ('ns', 'nt', 'nz')]
        nltk_noun = [each_word[0] for each_word in nltk.pos_tag(
            nltk.word_tokenize(each_line)) if each_word[1] in ('NNP', 'NNPS')]
        if jieba_noun != [] or nltk_noun != []:
            org.append(each_line.strip().decode('utf-8'))
    print 'File Name:', each_file
    print 'Name:', ';'.join(name)
    print 'Phone Num.:', ';'.join(phone_num)
    print 'Email:', ';'.join(email)
    print 'Org.:', ';'.join(org)
    print '-' * 15
