# 作业

## 综合分词工具和正则表达式提取邮件签名档

### 运行

```bash
cd mail_signature

python signature_extractor.py data_1.txt data_2.txt data_3.txt data_4.txt data_5.txt
```
### 输出结果

见 `result.txt`

### Drawback

1. 人名暂时放在第一行匹配，后续行不再匹配任命。
2. 单位匹配未用到regex，而jieba和nltk匹配精度不高，易把地址也匹配进。
