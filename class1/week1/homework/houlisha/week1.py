#-*- coding:utf-8 -*-

__author__='houlisha'

import os
import re
import codecs
import jieba
import jieba.posseg as pseg
from nltk.tag import StanfordNERTagger

os.environ['CLASSPATH'] = '/Users/maidoudou/Library/stanfordNLPLibrary/stanford-ner-2015-12-09'
os.environ['STANFORD_MODELS'] = '/Users/maidoudou/Library/stanfordNLPLibrary/stanford-ner-2015-12-09/classifiers'

stch = StanfordNERTagger('chinese.misc.distsim.crf.ser.gz')
sten = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')

divider_pattern = re.compile('--*')

tel_pattern = re.compile(r'(\+\d{2})?[ -]?\d{3,4}[ -]?\d{3,4}[ -]?\d{4,5}[-]?\d*')
def tel_match(data):
    iterator = tel_pattern.finditer(data)
    tels = [i.group() for i in iterator if iterator != None]
    return tels

mail_pattern = re.compile(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*')
def mail_match(data):
    iterator = mail_pattern.finditer(data)
    mails = [i.group() for i in iterator if iterator != None]
    return mails

# 中文姓名用jieba词性标注匹配
# 英文名字用nltk实体命名匹配
def name_match(data):
    ch_name = [w.word for w in pseg.cut(data) if w.flag == 'nr']
    en_name = [w[0] for w in sten.tag(data.split()) if w[1] == 'PERSON']
    return ch_name + en_name

# nltk效果不太好
def com_match(data):
    coms = []
    items = data.split('\n')
    for item in items:
        words = list(jieba.cut(item))
	ch_tags = stch.tag(words)
        ch_com = [w[0] for w in ch_tags if w[1] == 'ORG']
	if ch_com == []:
	    en_com = [w[0] for w in sten.tag(item.split()) if w[1] == 'ORGANIZATION']
	    if en_com == []:
	        continue
	coms.append(item)
    return coms

def signature_extract(datas):
    signatures = []
    for data in datas:
        signature = {}
        signature['name'] = name_match(data)
	signature['tel'] = tel_match(data)
	signature['email'] = mail_match(data)
	signature['com'] = com_match(data)

        signatures.append(signature)
    return signatures

def main():
    datafile = codecs.open('data.txt')
    datas = []
    data = ''
    line = datafile.readline()
    while line:
        if divider_pattern.match(line) != None: #another signature
	    datas.append(data)
	    data = ''
	else:
	    data = data + "\n" + line.strip()
	line = datafile.readline()
    if data != '':
        datas.append(data)

    signatures = signature_extract(datas)
    
    for signature in signatures:
        print '---------------------'
        print '姓名:' , " ".join(set(signature['name']))
        print '单位:' , " ".join(signature['com'])
        print '电话号码:' , signature['tel']
        print '电子邮箱:' , signature['email']
    
if __name__=='__main__':
    main()
