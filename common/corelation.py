#-*- coding: UTF-8 -*-
# coning = utf-8
__author__ = 'Aimee'
import json
from jsonpath_rw import jsonpath,parse
from common.connect_db import DB

relation_dict = {}
checksql_dict={}
class Correlation:
    def __init__(self):
        self.connect_db=DB()

    def is_relation(self,relation,res):

        #返回参数 res中的值赋予一个参数
        relation_para = [] #关联参数的左边  ${status}=status;${code}='200'
        relation_value = [] #关联参数的右边
        relation_json = [] #在res中找值
        if  relation != '':
            for i in relation.split(';'):
                relation_para.append(i.split('=')[0])
                relation_value.append(i.split('=')[1])

            for i in relation_value:
                json_exe = parse(i)
                madle = json_exe.find(res)
                if madle != None:
                    x = [math.value for math in madle][0]
                    if isinstance(x, int) or x == None:
                        x = str(x)
                    relation_json.append(x)

            for j in range(len(relation_para)):
                relation_dict[relation_para[j]] = relation_json[j]
        return relation_dict


   #数据sql
    '''
    connect_db:excel读取数据格式'${credit}=SELECT credit FROM star_user WHERE phone="13527231857";
    ${viewCount}=SELECT credit FROM star_user WHERE phone="13527231854"'
    '''
    def check_sql(self,connect_db):
        sql_expect_left = []
        sql_expect_right = []
        sql_expect_value = []
        if connect_db != '':

            for i in connect_db.split(';'):
                sql_expect_left.append(i.split('=', 1)[0])
                sql_expect_right.append(i.split('=', 1)[1])

            for i in range(len(sql_expect_right)):
                a = sql_expect_right[i]
                sql_expect_value.append(self.connect_db.select(a))

            for j in range(len(sql_expect_left)):
                checksql_dict[sql_expect_left[j]] = sql_expect_value[j].replace('[', '').replace(']', '').replace('"','')

        return checksql_dict

    def expect_check(self,expect,checksql_dict):
        if checksql_dict != {}:
            expect_left = []
            expect_right = []
            for i in expect.split(';'):
                expect_left.append(i.split('=', 1)[0])
                expect_right.append(i.split('=', 1)[1])

            for i in range(len(checksql_dict)):
                if str(expect_right).find(list(checksql_dict.keys())[i]) != -1:
                    expect_right = str(expect_right).replace(list(checksql_dict.keys())[i], list(checksql_dict.values())[i])
                    print(expect_right)
                    result = dict(zip(expect_left, eval(expect_right)))
                    return str(result).replace("': '",'=').replace("', '",';').replace("{'",'').replace("'}",'')
                else:
                    return expect
        else:
            return expect

    #执行delete sql
    def delete_sql(self,connect_db):
        if connect_db != '':
            for i in connect_db.split(';'):
                self.connect_db.delete(i)
        return 'ok'







if __name__ =="__main__":


    x = Correlation()

    expect = 'status=true;code=200;info.credit=${credit}'
    connect_db = 'DELETE FROM star_user WHERE phone="13177883232"'
    y=x.delete_sql(connect_db)
    print(y)












