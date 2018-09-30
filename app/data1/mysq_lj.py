import pymysql
from selenium.common.exceptions import NoSuchElementException
import logging

class Mysql_kybzhh():
    def dy(self):#读取mysql的mysql80的数据库里的kybzhh列表
        try:
            conn=pymysql.connect(host="localhost",user="root",password="root",database="mysql80",charset="utf8")
            #连接数据库
            #创建一个游标
            cursor=conn.cursor()
            #使用execute()方法执行sql语句
            cursor.execute("SELECT * FROM kybzhh")
            #打印全部数据给data
            data=cursor.fetchall()
        except (NoSuchElementException, Exception) as e:
            logging.error("错误原因%s"%str(e))#打印日志
        else:
            if(self):
                return data#返回data数据
            else:
                cursor.close()#关闭游标
                conn.close()#关闭数据库
    def shuju(self,a,b):
        try:
            data=Mysql_kybzhh().dy()
        except (NoSuchElementException, Exception) as e:
            logging.error("错误原因%s"%str(e))#打印日志
        else:
            return data[a][b]


if __name__ == '__main__':
    data=Mysql_kybzhh().shuju(0,1)
    print(data)

#学习python读取mysql数据网站：www.cnblogs.com/liubinsh/p/7568423.html
#https://www.cnblogs.com/dwenwen/articles/8259638.html





