# PostgreSQL 学习笔记

## 背景

- 知识图谱学习小组Week3的重点就是学习使用PostgreSQL+JSON, 作业是储存自己的W3C邮件JSON. 所以边做作业, 边记录自己整个的学习过程, 一是及时记录自己遇到的问题方便回顾, 二是希望过程可以复用, 帮助其他人少走些弯路.

- 具体关于为什么要选择PostgreSQL, 可以看看知识图谱学习小组的[wiki](https://github.com/memect/kg-beijing/wiki/%E7%AC%AC%E4%B8%80%E6%9C%9Fw3%EF%BC%9A%E7%9F%A5%E8%AF%86%E5%AD%98%E5%82%A8)
- [Why JSON in PostgreSQL is Awesome](https://functionwhatwhat.com/json-in-postgresql/)

## 安装并创建database
- 系统为Mac OS, 虽然在Download里找到了安装方法, 可是在官方文档的Installation里竟然没有给出具体的Mac系统下的安装方法. 表示不解. 难道大家上来不是先看官网文档?

         $ brew update; brew install postgres


- 初始化

         $ initdb -D /usr/local/pgsql/data


- 启动Server

         $ pg_ctl -D /usr/local/pgsql/data -l logfile start


- 创建database

        $ createdb mydb

- 删除database

        $ dropdb mydb

- 打开Database

        $ psql mydb

- 关闭Server

        $ kill -INT `head -1 /usr/local/pgsql/data/postmaster.pid`

每次启动关闭Server很麻烦, 可以把写个alias方便操作.

- 更简单的方法是直接下载[PostgreSQL.app](http://postgresapp.com/), 像安装应用一样, 启动和关闭server就是打开或关闭应用, 同时在`~/.bash_profile`中添加如下代码来设置PATH, 即可进行命令行交互.

         export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin


## psycopg2
- 安装psycopg2

         $ pip install pscopg2
    
    - 这里遇到了一点小坑:pscopg是依赖于PostgreSQL的, 所以只有在PostgreSQL装好后才可以安装.
    - 在调用过程中出现了如下错误

    > Library not loaded: libssl.1.0.0.dylib  
  Referenced from: /Users/xpgeng/anaconda/lib/python2.7/site-packages/psycopg2/_psycopg.so
  Reason: image not found
   
    - 原因是不能加载`libssl.1.0.0.dylib`, stackflow上有相关的答案
    - [How do I run psycopg2 on El Capitan without hitting a libssl error](http://stackoverflow.com/questions/32978365/how-do-i-run-psycopg2-on-el-capitan-without-hitting-a-libssl-error)
    - [import psycopg2 Library not loaded: libssl.1.0.0.dylib](http://stackoverflow.com/questions/27264574/import-psycopg2-library-not-loaded-libssl-1-0-0-dylib)
    - 但是第一个我使用了不好用, 方法就是建立`libssl.1.0.0.dylib`的symlink. 于是我用了第二个方法, 在`~/.bash_profile`中添加如下代码.
    
            export DYLD_FALLBACK_LIBRARY_PATH=$HOME/anaconda/lib/:$DYLD_FALLBACK_LIBRARY_PATH
            
    - Done!
 
- [Basic Module usage](http://initd.org/psycopg/docs/)
    - 如果你熟悉python的sqlite3, 想必再看psycopg2会很容易, 由于段老师已经非常详细的介绍了用法, 这里就不一一说明,具体请看[这里](https://github.com/memect/kg-beijing/tree/master/KG-PostgreSQL/KG-PostgreSQL).
    - 不过有些地方还想强调一下.
        - `conn.commit()`: 修改数据库后一定要记得提交...
          



## PostgreSQL 基本语法
### 常用命令
- 查看数据库列表: `user=#\l`
- 进入数据库: `user=#\c databasename`
- 查看数据库表结构: `user=#\d databasename`
- 退出: `user=#\q`

### 写入JSON
- 读取+ 创建TABLE

    ```python
    # -*- coding: utf-8 -*-
import json
import psycopg2
import psycopg2.extras  
    
    # Read data
    data = []
with open('W3C_data.json', 'r') as f:
    for line in f:
        data.append(json.loads(line, encoding='utf-8'))
f.close()

    # CREATE TABLE
conn = psycopg2.connect("dbname=W3C user=xpgeng")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    W3C(id serial primary key, data jsonb);
    ''')
    ```
- 写入数据. 这里从我遇到的坑入手写下如何写入JSON数据.
    - 直接将读取的字典写入到数据库失败
    - `str()`后出现如下问题
        
            psycopg2.DataError: invalid input syntax for type json  
            DETAIL:  Token "u" is invalid.  
            CONTEXT:  JSON data, line 1: {u... 
    - 我以为是编码的问题, 于是在读取JSON数据的时候加了 `encoding="utf-8"`, 还是不行.
    - Google 之后发现一个日文的[答案](http://symfoware.blog68.fc2.com/blog-entry-1258.html). 他使用了psycopg2.extras这个模块的method:Json. 于是采用之. 
    
    ```
    cursor.execute('''
        INSERT INTO W3C (data) VALUES (%s);
        ''', [psycopg2.extras.Json(item)])
    ```
    - 注意: `[]`很重要, 最开始受python语法的影响, 想当然的忘记了加`[]`, 走了弯路...
    - Done!

- Query.
   
   ```
   SELECT * FROM json_test WHERE data #> '{b,c}' = '"d"';
   ```
   - 这里只写了一个, 针对如下情况:

   > {"a": 1, "b": {"c": "d", "e": true}}
   
   - 通过这个语句我们就可以查询W3C中的信息.例如, headers->From = "Bobby Tung \<bobbytung@wanderer.tw>"
   
   ```
   SELECT data FROM W3C 
   WHERE data #> '{headers, From}' = '"Bobby Tung <bobbytung@wanderer.tw>"'
    ```

   - 还有很多姿势, 由于[Schinckel写的教程](http://schinckel.net/2014/05/25/querying-json-in-postgres/)已经非常完整, 大家可以继续深入学习.







## References
- PostgreSQL官方文档(这官方文档...呵呵)
    - <https://www.postgresql.org/download/macosx/>
    - [PostgreSql Official Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
    - [Install PostgeSQL on Mac OSX](https://www.postgresql.org/download/macosx/)
    - [GUI Tools of PostgreSQL.app](http://postgresapp.com/documentation/gui-tools.html)
    - [PostgreSql Official Documentation--8.14. JSON Types](https://www.postgresql.org/docs/current/static/datatype-json.html)
    - [PostgreSql Official Documentation--9.15. JSON Functions and Operators](https://www.postgresql.org/docs/current/static/functions-json.html)

- psysopg2
    - [psycopg2.extras](http://initd.org/psycopg/docs/extras.html)
        - Very Useful!! 
    - [Frequently Asked Questions](http://initd.org/psycopg/docs/faq.html)
- [Querying JSON in Postgres](http://schinckel.net/2014/05/25/querying-json-in-postgres/)
    - 大部分关于如何querying的语法, 代码都来自于这篇.
    - Schinchel 很厉害?
- [PostgreSQL JSON 数据类型--Author: Smallfish](http://chenxiaoyu.org/2014/07/25/postgresql-json.html)
 
- <http://stackoverflow.com/questions/21740359/python-mysqldb-typeerror-not-all-arguments-converted-during-string-formatting>
- <http://symfoware.blog68.fc2.com/blog-entry-1258.html>
- [有Python的地方, 就有大妈!!!](http://wiki.zoomquiet.io/pythonic/PsycopgJson)
   - 这是大妈写的关于psycopg2与json的文档.