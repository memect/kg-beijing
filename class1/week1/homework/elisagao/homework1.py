# encoding=utf-8
import jieba
import re

#get content from file
def get_file_content(file_name):
    fr = open(file_name, 'r')
    return fr
####写文件
def write_file(file_name, content):
    fw = open(file_name, 'w',encoding = 'utf-8')
    fw.writelines(content)
    fw.close()

file_name = 'emailsignature.txt'
text = get_file_content(file_name)
email_lines = 0
output_content = ""

for line in text:
    #person name
    if email_lines == 0:
        print (line)
        output_content += line 
        email_lines += 1
        continue
    if line.find("‐‐") == 0:
        email_lines = 0
        continue
    #company
    company_names = ["产业联合会", "技术社区", "律师事务所", "学校", "University"]
    flag_company_name = False
    for company_name in company_names:
        if line.find(company_name) != -1:
            print (line)
            output_content += line
            flag_company_name = True
            break
    if flag_company_name:
        continue            
    #phone number
    phone_words = ["Tel", "Mobile", "手机", "电话号码", "邮箱", "E‐mail", "mail", "地址", "+86"]
    flag_phone_word = False
    for phone_word in phone_words:
        if line.find(phone_word) == 0:
            print (line)
            output_content += line
            flag_phone_word = True
            continue
    if flag_phone_word:
        continue
    #email
    email_pattern = '\w*@\w*.\w*.\w*'
    if re.match(email_pattern, line):
        #print (re.match(email_pattern, line))
        print (line)
        output_content += line
        continue
    
    text = line
    seg_list = list(jieba.cut(line, cut_all=False))
    article_content = " ".join(list(seg_list))
    
    #address
    if article_content.find("中关村") != -1 and article_content.find("街") != -1 or article_content.find("Street") != -1:
        print (text)
        output_content += line
        #print ("done")
        continue
    #output_content += line 
write_file("output", output_content)



