#coding=utf-8
import pymysql

conn = pymysql.connect(
    host="172.31.12.26",
    port=3306,
    user="root",
    passwd="61g4WnqanM0B",
    db="python",
    charset="utf8"
)
#获取操作游标
cur = conn.cursor()

#aa = cur.execute("select * from test limit 10")
#print(aa)

#bb = cur.fetchone()
#print(bb)

#cc = cur.fetchmany(aa)
#for li in cc:
#    print(li)

cur.execute("insert into test VALUES (3,'ztwu3')")
aa = cur.execute("select * from test limit 10")
cc = cur.fetchmany(aa)
for li in cc:
    print(li)

cur.close()
#插入，修改事务提交
conn.commit()
conn.close()