# -*- coding:utf-8 -*-
import sys
import re
import json
import mailbox
from Mail2Json import Mail2Json

mailbox = mailbox.mbox('2013-11.mbx')
for message in mailbox:
    message_string = message.as_string()
    m2j = Mail2Json(message_string=message_string)
    mail_id = m2j.GetMessageId()['MessageId'].encode('utf-8')
    mail_json = m2j.GetAll()
    json.dump(mail_json, open('parse_result\\' + '%s.json' % mail_id, 'w'), ensure_ascii=False)
