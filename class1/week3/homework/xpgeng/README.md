# 用PostgreSQL储存W3C-JSON数据

## Tutorial
- 安装好PostgreSQL

         $ brew update; brew install postgres


- 初始化

         $ initdb -D /usr/local/pgsql/data


- 启动Server

         $ pg_ctl -D /usr/local/pgsql/data -l logfile start


- 创建database

        $ createdb W3C

    - 更简单的方法是直接下载[PostgreSQL.app](http://postgresapp.com/), 像安装应用一样, 启动和关闭server就是打开或关闭应用, 同时在`~/.bash_profile`中添加如下代码来设置PATH, 即可进行命令行交互.

         export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin

- 下载所有本文件夹的后运行`W3C.py`
    - 注意要提前修改好`W3C.py`中数据库相关代码
- 运行`W3C_query.py`. 可以根据自己的查询需要, 修改代码.
    - 具体简称见`PostgreSQL_note.md`


## Author
- [耿新鹏](https://github.com/xpgeng)
