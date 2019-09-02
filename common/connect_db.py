# coning = utf-8
__author__ = 'Aimee'
import pymysql
import config.readConfig as conf
from common import loger
import json

host =conf.ReadConfig().get_db('host')
user =conf.ReadConfig().get_db('username')
password =conf.ReadConfig().get_db('password')
port =conf.ReadConfig().get_db('port')
db =conf.ReadConfig().get_db('database')
log = loger.Log()

class DB():
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host= str(host) ,
                user=user,
                port=int(port),
                password=password,
                database=db,
                charset='utf8'
                )
        except Exception as e:
            log.error("数据库连接错误：出错是:%s" %e )

     #查询所有数据
    def select(self,sql):
        cusor = self.conn.cursor()
        cusor.execute(sql)
        result = cusor.fetchone()
        return json.dumps(result)

    #删除数据,修改，插入
    def delete(self,sql):
        cusor = self.conn.cursor()
        try:
            log.info('执行sql语句')
            cusor.execute(sql)
            self.conn.commit()
        except Exception as e:
            log.error("执行sql错误回滚：出错原因是：%s" %e)
            self.conn.rollback()




    def close(self):
        self.conn.close()


if __name__ =="__main__":
    x = DB()
    z = 'DELETE FROM star_user WHERE phone="13177886633"'
    z1 ='SELECT id FROM star_gift WHERE `status`=1 AND gift_type=2 LIMIT 1'

    y = x.delete(z)
    y1= x.select(z1)
    print(y,y1)




