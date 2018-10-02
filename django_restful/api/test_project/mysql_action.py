from pymysql import connect#导入connect连接数据库的模块
import yaml#导入yaml，做数据封装
import logging


class DB():
    def __init__(self):#连接数据库
        logging.info('==================init data===============')#打印日志
        logging.info('connect db...')#打印日志
        self.conn = connect(host='127.0.0.1', user='root', password='root', db='django_restful')#连接数据库，db这个是连接的数据库名

    def clear(self, table_name):#清除表中的数据方法
        logging.info('clear db...')
        clear_sql = 'truncate ' + table_name + ';'#这个是清除数据的方法，truncate+表名;
        with self.conn.cursor() as cursor:#定义一个游标
            cursor.execute('set foreign_key_checks=0;')#执行set foreign_key_checks=0方法是清除一些外界的因素，比如：个个表可能有些依赖，所以首先先清除掉
            cursor.execute(clear_sql)#执行clear_sql这个方法
        self.conn.commit()#commit()是提交执行

    def insert(self, table_name, table_data):#插入数据的方法
        logging.info('inser data...')
        for key in table_data:#把table_data的字典类型数据全部读取出来并且
            table_data[key] = "'" + str(table_data[key]) + "'"

        key = ','.join(table_data.keys())#把所有keys值读取出来，前面并且加,
        value = ','.join(table_data.values())#把table_data的values值取出来，因为value值已经加了单引号

        logging.info(key)#把所有key值打印出来
        logging.info(value)

        insert_sql = 'insert into '+ table_name + '('+key+')'+' values'+'('+value+')'#这个是插入数据的sql方法insert into 表名（字段,字段1）values（数据,数据1）
        print(insert_sql)
        logging.info(insert_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(insert_sql)
        self.conn.commit()

    def close(self):#关闭数据库方法，
        logging.info('close db')
        self.conn.close()#conn.close()是关闭数据库
        logging.info('=============init finished!============')

    def init_data(self, datas):#数据初始化方法
        for table, data in datas.items():#table是读取yaml文件的表名如：api_user，data是读取yaml文件里的数据，如：api_user里的数据id，username这些
            #items()方法例子：http://www.runoob.com/python3/python3-att-dictionary-items.html
            self.clear(table)#对table这个表的内容进行清除操作先
            for d in data:#然后进行for循环读取data的数据
                print(d)
                self.insert(table, d)#然后调用插入的方法
        self.close()

    def test_cz(self):
        db=DB()
        f = open('datas.yaml', 'r')
        datas = yaml.load(f)
        db.init_data(datas)


if __name__ == '__main__':
    db = DB()
    # db.clear('api_user')
    # db.clear('api_group')
    #user_data={'id':1,'username':'zxw2018','email':'zxw2018@163.com'}
    #db.insert('api_user',user_data)
    #db.close()

    f = open('datas.yaml', 'r')
    datas = yaml.load(f)
    db.init_data(datas)