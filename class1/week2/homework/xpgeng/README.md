# Week2 Homework

## Introduction
- 选择的JSON来储存数据
- 数据的格式为


> - `headers`: 这部分包含从MIME头提取的信息, 如'From', 'Receive', 'Send_time', 'Subject'等等  
> - `content`: 这部分会包含所有的内容信息, 如'Body\_text', 'Body\_html', 'Recite', 'Attachment', 'Signature'等等
> - `entity`: 包含邮件中提到的各种实体, 如'Name', 'Organization', 'Time', 'Position', 'Tel'
> - `relation`: 包含邮件内的各种关系, 如邮件之间的关系, 邮件内容的语义关系.

- 目前`Entities`, `Relation`做的还远远不够, 更深入的原因是无从下手, 尤其是关系的提取, 这也是以后要深入学习的地方.
- 基本上知识的粒度本着层层递进的原则
    - 一开始是比较容易提取的Metadata
    - 然后需要花些时间提取的如签名档等内容
    - 接着是细化到NER
    - 最后再上升到关系(这里就只是给了个In-Reply-To, 随着学习的深入, 一定会在深入挖掘, 不断完善)

## Example

```json

{
    "content": {
        "(text/html)": "<div dir=\"ltr\">css-text \u7684 4.1.2. Segment Break Transformation Rules<div>\u4e2d\u5199\u5230\uff1aif the East Asian Width property <a href=\"http://dev.w3.org/csswg/css-text/#ref-UAX11\" rel=\"biblioentry\">[UAX11]</a> of both the character before\r\n    and after the line feed is F, W, or H (not A), and neither side is\r\n    Hangul, then the segment break is removed.</div><div><br></div><div>\u8fd9\u91cc\u8981\u6c42segment break\uff08\u5373\u6362\u884c\uff09\u4e24\u8fb9\u90fd\u662f\u6c49\u5b57\u7b26\u53f7\uff08Unicode\u89c4\u8303\u4e2d\u7684East Asian Width\u5c5e\u6027\u662fFullwidth\u3001Wide\u3001Halfwidth\uff09\u624d\u4f1a\u53bb\u6389\uff0c\u4e5f\u5c31\u610f\u5473\u7740\u6c49\u5b57\u548c\u67d0\u4e9b\u5c5e\u6027\u4e3a<i>Ambiguous</i>\u7684\u7b26\u53f7\uff08\u5982\u5f15\u53f7\u3001\u00a5\u7b26\u53f7\u7b49\uff09\u4e4b\u95f4\u7684\u7a7a\u767d\u4e0d\u4f1a\u88abremove\u800c\u4ecd\u7136\u662f\u53d8\u6210\u4e00\u4e2a\u7a7a\u683c\u3002</div>\r\n<div><br></div><div>\u4e5f\u5c31\u662f\u662f\u8bf4\u8fd9</div><div>\u6bb5\u6587\u5b57\u4e2d\u7684\u6362</div><div>\u884c\u90fd\u4f1a\u88ab\u53bb\u6389\uff0c</div><div>\u7136\u800c\u5982\u679c\u662f\u5728</div><div>\u201c\u5f15\u53f7\u524d\u540e\u7684\u6362\u884c\u201d</div><div>\u6216\u8005\u662f\u65e5\u5143\u7b26\u53f7</div><div>\u00a5\u524d\u7684\u6362\u884c\u5c31\u4e0d</div><div>\u4f1a\u53bb\u6389\u3002</div><div><br></div><div>\u6211\u8ba4\u4e3a\u8fd9\u4e2a\u4e0d\u592a\u597d\u3002\u5efa\u8bae\u5c06\u89c4\u5219\u6539\u4e3a\u5982\u679c\u4e24\u4e2a\u5b57\u7b26\u4e00\u4e2a\u662fA\u53e6\u4e00\u4e2a\u662fF\u3001W\u3001H\u7684\u65f6\u5019\u4e5f\u53bb\u6389\u7a7a\u683c\u3002</div>\r\n<div><br></div><div><br></div><div><br></div></div><div class=\"gmail_extra\"><br><br><div class=\"gmail_quote\">2013/11/14 \u8463\u798f\u8208 Bobby Tung <span dir=\"ltr\">&lt;<a href=\"mailto:bobbytung@wanderer.tw\" target=\"_blank\">bobbytung@wanderer.tw</a>&gt;</span><br>\r\n<blockquote class=\"gmail_quote\" style=\"margin:0 0 0 .8ex;border-left:1px #ccc solid;padding-left:1ex\">\u5404\u4f4d\uff1a<br>\r\n<br>\r\n\u30fbCSS Text Module Level 3\uff1a<br>\r\n[\u539f\u6587]: <a href=\"http://www.w3.org/TR/css3-text/\" target=\"_blank\">http://www.w3.org/TR/css3-text/</a><br>\r\n[\u7ffb\u8b6f 3%]: <a href=\"http://www.w3.org/html/ig/zh/wiki/Css4-text\" target=\"_blank\">http://www.w3.org/html/ig/zh/wiki/Css4-text</a><br>\r\n<br>\r\n\u30fbCSS Writing Module Level 3\uff1a<br>\r\n[\u539f\u6587]: <a href=\"http://www.w3.org/TR/css3-text/\" target=\"_blank\">http://www.w3.org/TR/css3-text/</a><br>\r\n[\u7ffb\u8b6f]: <a href=\"http://www.w3.org/html/ig/zh/wiki/Css3-writing-modes\" target=\"_blank\">http://www.w3.org/html/ig/zh/wiki/Css3-writing-modes</a><br>\r\n<br>\r\n\u9019\u5169\u4efd\u6587\u4ef6\u5df2\u7d93\u9032\u5165Last Call\uff0c\u5f9e\u4eca\u5929\u8d77\u516d\u5468\u5167\u70baReview\u671f\u3002<br>\r\n<br>\r\n\u6211\u5011\u53ef\u4ee5\u505a\u7684\u6709\u5169\u4ef6\u4e8b\uff1a<br>\r\n<br>\r\n1, \u7ffb\u8b6f<br>\r\n<br>\r\n2, \u8b80\u539f\u6587\uff0c\u770b\u770b\u6709\u6c92\u6709\u4efb\u4f55\u554f\u984c\uff0c\u82e5\u6709\uff0c\u8acb\u5728\u9019\u4e32\u8a0e\u8ad6\uff0c\u532f\u6574\u5f8c<br>\r\n<br>\r\n\u7ffb\u8b6f\u63d0\u51fa\uff0c\u6216\u8005\u76f4\u63a5\u56de\u8986\u5230 &nbsp;<a href=\"mailto:www-style@w3.org\">www-style@w3.org</a> \u8a0e\u8ad6\u3002<br>\r\n<br>\r\n<br>\r\nWANDERER Digital Publishing Inc.<br>\r\nBobby Tung<br>\r\nMobile\uff1a+886-975068558<br>\r\n<a href=\"mailto:bobbytung@wanderer.tw\">bobbytung@wanderer.tw</a><br>\r\nWeb\uff1a<a href=\"http://wanderer.tw\" target=\"_blank\">http://wanderer.tw</a><br>\r\n<br>\r\n<br>\r\n</blockquote></div><br></div>\r\n", 
        "(text/plain)": "css-text \u7684 4.1.2. Segment Break Transformation Rules\r\n\u4e2d\u5199\u5230\uff1aif the East Asian Width property\r\n[UAX11]<http://dev.w3.org/csswg/css-text/#ref-UAX11>of both the\r\ncharacter before and after the line feed is F, W, or H (not A),\r\nand neither side is Hangul, then the segment break is removed.\r\n\r\n\u8fd9\u91cc\u8981\u6c42segment break\uff08\u5373\u6362\u884c\uff09\u4e24\u8fb9\u90fd\u662f\u6c49\u5b57\u7b26\u53f7\uff08Unicode\u89c4\u8303\u4e2d\u7684East Asian\r\nWidth\u5c5e\u6027\u662fFullwidth\u3001Wide\u3001Halfwidth\uff09\u624d\u4f1a\u53bb\u6389\uff0c\u4e5f\u5c31\u610f\u5473\u7740\u6c49\u5b57\u548c\u67d0\u4e9b\u5c5e\u6027\u4e3a*Ambiguous*\r\n\u7684\u7b26\u53f7\uff08\u5982\u5f15\u53f7\u3001\u00a5\u7b26\u53f7\u7b49\uff09\u4e4b\u95f4\u7684\u7a7a\u767d\u4e0d\u4f1a\u88abremove\u800c\u4ecd\u7136\u662f\u53d8\u6210\u4e00\u4e2a\u7a7a\u683c\u3002\r\n\r\n\u4e5f\u5c31\u662f\u662f\u8bf4\u8fd9\r\n\u6bb5\u6587\u5b57\u4e2d\u7684\u6362\r\n\u884c\u90fd\u4f1a\u88ab\u53bb\u6389\uff0c\r\n\u7136\u800c\u5982\u679c\u662f\u5728\r\n\u201c\u5f15\u53f7\u524d\u540e\u7684\u6362\u884c\u201d\r\n\u6216\u8005\u662f\u65e5\u5143\u7b26\u53f7\r\n\u00a5\u524d\u7684\u6362\u884c\u5c31\u4e0d\r\n\u4f1a\u53bb\u6389\u3002\r\n\r\n\u6211\u8ba4\u4e3a\u8fd9\u4e2a\u4e0d\u592a\u597d\u3002\u5efa\u8bae\u5c06\u89c4\u5219\u6539\u4e3a\u5982\u679c\u4e24\u4e2a\u5b57\u7b26\u4e00\u4e2a\u662fA\u53e6\u4e00\u4e2a\u662fF\u3001W\u3001H\u7684\u65f6\u5019\u4e5f\u53bb\u6389\u7a7a\u683c\u3002\r\n\r\n\r\n\r\n\r\n\r\n2013/11/14 \u8463\u798f\u8208 Bobby Tung <bobbytung@wanderer.tw>\r\n\r\n> \u5404\u4f4d\uff1a\r\n>\r\n> \u30fbCSS Text Module Level 3\uff1a\r\n> [\u539f\u6587]: http://www.w3.org/TR/css3-text/\r\n> [\u7ffb\u8b6f 3%]: http://www.w3.org/html/ig/zh/wiki/Css4-text\r\n>\r\n> \u30fbCSS Writing Module Level 3\uff1a\r\n> [\u539f\u6587]: http://www.w3.org/TR/css3-text/\r\n> [\u7ffb\u8b6f]: http://www.w3.org/html/ig/zh/wiki/Css3-writing-modes\r\n>\r\n> \u9019\u5169\u4efd\u6587\u4ef6\u5df2\u7d93\u9032\u5165Last Call\uff0c\u5f9e\u4eca\u5929\u8d77\u516d\u5468\u5167\u70baReview\u671f\u3002\r\n>\r\n> \u6211\u5011\u53ef\u4ee5\u505a\u7684\u6709\u5169\u4ef6\u4e8b\uff1a\r\n>\r\n> 1, \u7ffb\u8b6f\r\n>\r\n> 2, \u8b80\u539f\u6587\uff0c\u770b\u770b\u6709\u6c92\u6709\u4efb\u4f55\u554f\u984c\uff0c\u82e5\u6709\uff0c\u8acb\u5728\u9019\u4e32\u8a0e\u8ad6\uff0c\u532f\u6574\u5f8c\r\n>\r\n> \u7ffb\u8b6f\u63d0\u51fa\uff0c\u6216\u8005\u76f4\u63a5\u56de\u8986\u5230  www-style@w3.org \u8a0e\u8ad6\u3002\r\n>\r\n>\r\n> WANDERER Digital Publishing Inc.\r\n> Bobby Tung\r\n> Mobile\uff1a+886-975068558\r\n> bobbytung@wanderer.tw\r\n> Web\uff1ahttp://wanderer.tw\r\n>\r\n>\r\n>\r\n", 
        "Signature": "Bobby Tung\r\nMobile\u00ef\u00bc\u0161+886-975068558\nbobbytung@wanderer.tw\r\nWeb\u00ef\u00bc\u0161http://wanderer.tw\n\n\n\n"
    }, 
    "entity": {
        "Name": [
            "\u8463\u798f\u8208"
        ], 
        "Organization": []
    }, 
    "headers": {
        "Cc": "W3C HTML5 \u4e2d\u6587\u8208\u8da3\u5c0f\u7d44 <public-html-ig-zh@w3.org>", 
        "Date": "Thu, 14 Nov 2013 23:48:05 +0800", 
        "From": "John Hax <johnhax@gmail.com>", 
        "Subject": "Re: CSS Text Module Level 3, CSS Writing Module Level 3 Last Call", 
        "To": "\u8463\u798f\u8208 Bobby Tung <bobbytung@wanderer.tw>"
    }, 
    "relation": {
        "In-Reply-To": "<54A54A48-3934-4AEA-ACA1-DF84B06C578A@wanderer.tw>"
    }
}

```

## Author
- [耿新鹏](https://github.com/xpgeng)