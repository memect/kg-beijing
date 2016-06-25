# 作业

## 自己设计电子邮件的结构化表示

### 已解析的部分

| 字段          | 解释           |
|-------------  |------------   |
| MessageId     | 邮件ID         |
| Subject       | 主题           |
| Date          | 日期           |
| InReplyToId   | 回复ID         |
| Body          | 主体内容       |
| MimeVersion   | 版本           |
| ContentType   | 段体类型       |
| From          | 各发件人名称:邮件地址 |
| To            | 各收件人名称:邮件地址 |
| Cc            | 各抄送人名称:邮件地址 |
| Bcc           | 各密送人名称:邮件地址 |

### 未解析的部分

| 字段          | 解释           |
|-------------  |------------   |
| Attachment    | 附件           |
| Content       | 段体内容       |
| Quote         | 引用           |
| Signature     | 签名档         |
| SemanticRelationship | 语义关系       |

### 运行

```bash
cd Mbox_KP

python parse_mbx.py
```
### 输出结果

见 `Mbox_KP\parse_result` 文件夹下各邮件json解析结果

### 心得

1. 邮件头还不是很难解析，有个别收发件人姓名地址有部分缺失需要注意。
2. 暂时没找到层级提取邮件、签名档的方法。
