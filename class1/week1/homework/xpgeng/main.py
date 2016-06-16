# -*- coding: utf-8 -*-

import os
import re
import jieba
import jieba.posseg as pseg
import pynlpir
from nltk.tag import StanfordNERTagger

# Add models of NLTK  
os.environ["CLASSPATH"] = "/Users/xpgeng/Library/stanford-ner-2015-12-09"  
os.environ["STANFORD_MODELS"] = "/Users/xpgeng/Library/stanford-ner-2015-12-09/models"

# Load user dict
jieba.load_userdict('user_dict.txt')


def judge_lang(words):
    '''
    Parameters: Someone's signature (str)
    Return: Language
    '''
    word_list = filter(None, re.split(r',|\s+', words))
    for word in word_list:
        if not word.isalpha():
            return "Chinese"
        else:
            return "English"

def extract_information(signature, language, st):
    '''
    Parameters: 
        signature: str
        language: "Chinese" or "English"
        st: Stanford Tagger
    Return:
        information_dict: dict
    '''
    words_list = re.split(r'\n|\|', signature)    # split signature by \n, |
    orgnization_list = []
    tel_list = []
    email_list = []
    name_list = []
    
    p_email = re.compile(r'\w+@(\w+\.)+(\w+)')
    p_tel = re.compile(r'''(\+([\d|\s]+)) # +86 132 2345 2345
                   | (电话.+([\d|\s|\-]+))
                   | (Tel.+([\d|\s|\-]+))
                   | (手机.+([\d|\s|\-]+))
                   | Mobile.+([\d|\s|\-]+)''', re.VERBOSE)
    
    for item in words_list:
        
        # Extract tel list
        if p_tel.search(item): 
            tel_group = p_tel.search(item).group()
            tel_list.append(tel_group) 
        
        # Extract email list
        elif p_email.search(item):
            m = p_email.search(item).group()
            email_list.append(m) 
            
        # Extract name and orgnization from Chinese signature
        elif language == "Chinese":
            words = pseg.cut(item)
            flag_list = [flag for word, flag in words]
            if 'nt' in flag_list:
                orgnization_list.append(item)
            elif 'nr'in flag_list:
                name_list.append(item)
        
        # Extract name and orgnization from English signature
        elif language == "English":
            flag_list = [flag for word, flag in st.tag(item.split())]
            if 'ORGANIZATION' in flag_list:
                orgnization_list.append(item)
            elif 'PERSON' in flag_list:
                name_list.append(item)
        else:
            return "Nothing to extract!"
    
    information_dict = {"name": list(set(name_list)), "tel": tel_list, 
                        "email": email_list, "orgnization": orgnization_list}
    return information_dict         

def main(data):
    p = re.compile(r'-{2,}')
    signature_list = p.split(data)

    # Add Tagger
    st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')

    # Write to result.txt
    with open('result.txt', 'a') as f:
        for signature in signature_list:
            info_dict = extract_information(signature, judge_lang(signature), st)
            name = '姓名: {name}'.format(name=info_dict['name'][0])
            organization = '单位:'
            for item in info_dict['orgnization']:
                organization += "%s " % item
            tel = ''
            for item in info_dict['tel']:
                tel += "%s\t" %item
            email = "Email: %s" % info_dict['email']
            info = '%s\n%s\n%s\n%s\n-------\n'% (name, organization, tel, email)
            f.write(info)
            print info
    print "Done! Save into result.txt..."
    f.close()

if __name__ == '__main__':
    # Read data
    with open('data.txt', 'r') as f:
        data = f.read()
    main(data)