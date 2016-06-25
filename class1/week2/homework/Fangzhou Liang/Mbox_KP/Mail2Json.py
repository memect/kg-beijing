# -*- coding:utf-8 -*-
import sys
import re
import json
from flanker import mime

mail_address_with_name_regex = re.compile(
    r'((?<!>),*[^<>]+)+(<(([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5}))>)?')
mail_address_regex = re.compile(
    r'([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})')


class Mail2Json(object):

    def __init__(self, message_string):
        self.message_string = message_string
        self.FKmsg = mime.from_string(self.message_string)

    def GetMessageId(self):
        MessageId = self.FKmsg.message_id
        return {'MessageId': MessageId}

    def GetSubject(self):
        Subject = self.FKmsg.subject \
            if self.FKmsg.subject is not None else None
        return {'Subject': Subject}

    def GetDate(self):
        Date = self.FKmsg.headers['Date']
        return {'Date': Date}

    def GetInReplyToId(self):
        InReplyToId = self.FKmsg.headers['In-Reply-To'] \
            if self.FKmsg.headers['In-Reply-To'] is not None else None
        return {'InReplyToId': InReplyToId}

    def GetBody(self):
        Body = self.FKmsg.body \
            if self.FKmsg.body is not None else None
        return {'Body': Body}

    def GetMimeVersion(self):
        MimeVersion = self.FKmsg.headers['MIME-Version']
        return {'MimeVersion': MimeVersion}

    def GetContentType(self):
        return {'ContentType': self.FKmsg.content_type}

    def __MailAddressParse(self, MailAddressString):
        man_tuple = mail_address_with_name_regex.findall(MailAddressString)
        tmp_list = []
        for one in man_tuple:
            name = one[0].replace('\'', '').replace('\"', '').strip()
            email = one[2] if one[2] != '' else None
            if mail_address_regex.match(name) and email == None:
                email = name
            tmp_list.append({name: email})
        return tmp_list

    def GetFrom(self):
        From_list = self.__MailAddressParse(
            MailAddressString=self.FKmsg.headers['From'])
        return {'From': From_list}

    def GetTo(self):
        To_list = self.__MailAddressParse(
            MailAddressString=self.FKmsg.headers['To'])
        return {'To': To_list}

    def GetCc(self):
        cc = self.FKmsg.headers['Cc']
        if cc is None:
            return {'Cc': None}
        else:
            Cc_list = self.__MailAddressParse(MailAddressString=cc)
            return {'Cc': Cc_list}

    def GetBcc(self):
        bcc = self.FKmsg.headers['Bcc']
        if bcc is None:
            return {'Bcc': None}
        else:
            Bcc_list = self.__MailAddressParse(MailAddressString=bcc)
            return {'Bcc': Bcc_list}

    def GetAll(self):
        return json.dumps(
            dict(
                self.GetMessageId().items() +
                self.GetInReplyToId().items() +
                self.GetSubject().items() +
                self.GetDate().items() +
                self.GetMimeVersion().items() +
                self.GetContentType().items() +
                self.GetBody().items() +
                self.GetFrom().items() +
                self.GetTo().items() +
                self.GetCc().items() +
                self.GetBcc().items()
            ), ensure_ascii=False).encode('utf8')
