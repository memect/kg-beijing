# PostgreSQL 学习笔记

## 安装
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


## 利用psycopg2与PostgreSQL交互
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
    - 但是第一个我使用了不好用, 方法就是建立`libssl.1.0.0.dylib`的symlink. 于是我用了第二个方法.
    
            export DYLD_FALLBACK_LIBRARY_PATH=$HOME/anaconda/lib/:$DYLD_FALLBACK_LIBRARY_PATH
            
    - Done!
 
- [Basic Module usage](http://initd.org/psycopg/docs/)
    - 如果你熟悉python的sqlite3, 想必再看psycopg2会很容易, 由于段老师已经非常详细的介绍了用法, 这里就不一一说明,具体请看[这里](https://github.com/memect/kg-beijing/tree/master/KG-PostgreSQL/KG-PostgreSQL).
    - 不过有些地方还想强调一下.
        - `conn.commit()`: 修改数据库后一定要记得提交... 





## References
- <https://www.postgresql.org/download/macosx/>
- [PostgreSql Official Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
- [Install PostgeSQL on Mac OSX](https://www.postgresql.org/download/macosx/)
- [GUI Tools of PostgreSQL.app](http://postgresapp.com/documentation/gui-tools.html)