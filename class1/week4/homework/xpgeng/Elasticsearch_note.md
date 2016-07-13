# Elasticsearch 学习笔记

##

## 安装
- 下载.[链接](https://www.elastic.co/thank-you?url=https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/zip/elasticsearch/2.3.3/elasticsearch-2.3.3.zip)
- 解压
- 使用下面的命令, 开启服务.

    > cd bin  
    > ./elasticsearch

- 检测安装是否成功.
    - 重新打开一个Terminal, 输入命令

        > curl -X GET http://localhost:9200/
    
    - 此时如果安装成功会返回一个JSON信息.



## References
- [Installing Elasticsearch on Mac OS X](http://codingexplained.com/operating-systems/mac/installing-elasticsearch-mac-os-x)