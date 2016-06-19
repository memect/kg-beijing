import re,nltk,jieba
import jieba.posseg as pseg
from bs4 import BeautifulSoup as bs
with open("F:\python\KGhomework\maildata.txt","r") as fp:
	mail_con = fp.read()
	pattern = re.compile(r"[-]{2,}")
	str_list = pattern.findall(mail_con)
	mail_list = mail_con.split(str_list[0])
	for mail in mail_list:
		mail_iterms = [i for i in mail.split('\n') if i != '' ]
		names = mail_iterms[0]    #姓名一般都在第一项
		#print(names)
		pattern1 = re.compile(r'[\d][\d\s-]+')
		pattern2 = re.compile(r'(:|：)')
		pho_nums = [pattern1.search(j).group() for j in mail_iterms if re.findall(r'(电话|手机|Mobile|[+]).*[:]?\d+',j)]
		emails = [m.split("|")[-1].split(':')[-1].split('：')[-1] for m in mail_iterms if re.search(r'[(邮箱|E-mail|Email)]?[:]?[\w\.]+@[\w\.]+',m)] 
		'''采用jieba自定义字典'''
		for x in mail_iterms: 
			jieba.load_userdict("userdict.txt")	
			words = pseg.cut(x)
			#org = [word  for word, flag in words if flag in ['nz','nt'] ]
			for word, flag in words :
				if flag in ['nz','nt']:
					data= {
						"name": names,
						"tel": pho_nums,
						"email": emails,
						"orgnization": word
					}
					print(data)
		'''****不知道如何适当应用*******'''		
		words = nltk.word_tokenize(x)
		tokens = nltk.pos_tag(words)
		grammar = "NP: {<NNP>+(<CC>|<IN>)<NNP>+}"
		cp = nltk.RegexpParser(grammar)
		result = cp.parse(tokens)
		org1 = nltk.ne_chunk(tokens)
					
			
		
	
	
		