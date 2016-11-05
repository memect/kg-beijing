# 程序基于py3
# 未完成持续更新中
import re
import re_ex
import jieba


re_phone = re.compile(re_ex.phone_ex)
re_mail = re.compile(re_ex.email_ex)


def extract_org(signature):
    '''自定义公司实体抽取函数'''

    cand = []
    for l in signature:
        new_l = re.sub('[\WA-Za-z]+', '', l)
        token_len = len(list(jieba.cut(new_l)))
        str_len = len(l)
        if token_len and str_len:
            cand.append((l, token_len, str_len))

    ranked = sorted(cand, key=lambda x:x[2]/x[1])
    return ranked[1][0] if len(ranked) > 1 else ''


def extract_entity(signature):
    '''从签名档中提取指定实体'''
    lines = [l.strip() for l in signature.split('\n')]

    infos = {}
    infos['name'] = lines[0]
    infos['company'] = extract_org(lines[1:])
    infos['phone'] = []
    infos['mail'] = ''

    for l in lines:
        l = l.strip()
        phone = re_phone.search(l)
        if phone:
            infos['phone'].append(phone.group())

        mail = re_mail.search(l)
        if mail:
            infos['mail'] = mail.group()

    return infos

def test_extract_entity():
    mark = ['''刘三 Liu, San
        +86 15912348765
        sfghsdfg@abc.org.cn
        ''',
        '''李四
        北清大数据产业联合会
        电话：010-34355675
        邮箱：lisi@beiqingdata.com
        地址：北京市海淀区北清大学东楼201室
        ''',
        '''John Smith
        Data and Web Science Group
        University of Mannheim, Germany

        http://dws.informatik.uni-mannheim.de/~johnsmith
        Tel: +49 621 123 4567
        ''',
        '''王五
        CSDN-全球最大中文IT技术社区（www.csdn.net）
        电话:010-51661202-257
        手机:13934567890
        E-mail:gdagsdfs@csdn.net
        QQ、微信：34534563
        地址：北京市朝阳区广顺北大街33号院一号楼福码大厦B座12层
        ''',
        '''张三
        北京市张三律师事务所|Beijing Zhangsan Law Firm
        北京市海淀区中关村有条街1号，邮编：100080
        No. 1 Youtiao Street , ZhongGuanCun West, Haidian District, Beijing 100080
        Mobile: 15023345465|Email: dfgasedt@126.com''']
    for e in mark:
        print(extract_entity(e))
        # extract_entity(e)


if __name__ == '__main__':
    test_extract_entity()
