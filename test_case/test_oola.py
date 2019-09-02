# coning = utf-8
__author__ = 'Aimee'
import unittest,json
from ddt import ddt,data
from common.myHttp import MyHttp
from common.duanyan import DuanYan
from common.get_token import GetToken
from common.operation_json import OperationJson
from common.send_mail import sendEmail
from common.corelation import Correlation
from common.do_excel import OperationExcel
from config.readConfig import ReadConfig
from common.loger import Log
from common.connect_db import DB
from common.update_params import *
loging = Log()

#读取用例数据
test_data =OperationExcel().read_excel_to_dict()

info = ReadConfig()
baseurl = info.get_http('baseurl')


# global relation_dict
# global pass_count
# global fail_count
global filepath
relation_dict = {}
relation_dict1 = {}
pass_count=[]
fail_count =[]
@ddt
class Oola_testCase(unittest.TestCase):
    def setUp(self):
        loging.info('测试开始')
        self.run_method = MyHttp()
        self.data = OperationExcel()
        self.duanyan = DuanYan()
        self.sendmail = sendEmail()
        self.relaton = Correlation()
        self.connect_db = DB()

    @data(*test_data)
    def test_oola(self,value): #定义一个变量来接收ddt.data中的数据
        if value['run'] == 'yes':
            loging.info('目前正在执行第%s条用例' %value['id'])
            loging.info('请求方式：%s' % value['method'])
            global relation_dict
            global relation_dict1
            global pass_count
            global fail_count

            method =value['method']
            url = baseurl+value['url']
            data=update_params(value,relation_dict1)


            if value['是否携带header'] =='write':
                res = self.run_method.run_main(method, url, data)
                token = GetToken(res)
                token.write_token()
            elif value['是否携带header'] == 'yes':
                op_json = OperationJson('../test_data/token.json')
                token = op_json.get_data('token')
                header = {
                    'token': token
                }
                res = self.run_method.run_main(method, url, data, header)
            else:
                res = self.run_method.run_main(method, url, data)
            loging.info('请求参数 %s' % value['params'])
            loging.info('返回响应 %s' % res)

            # 关联数据
            relation = value['corelation']
            relation_dict = self.relaton.is_relation(relation, res)


            #关联sql
            connect_db = value['sql_select']
            checksql_dict = self.relaton.check_sql(connect_db)


            #checksql_dict合并到relation_dict
            relation_dict1 = relation_dict.copy()
            if checksql_dict !=None:
             relation_dict1.update(checksql_dict)

            #写入res数据
            self.data.write_Response(int(value['id']),json.dumps(res).encode('utf-8').decode('unicode_escape'))



            # 断言判断
            expect = value['expect']
            expect_sql = self.relaton.expect_check(expect,checksql_dict)

            #删除sql
            sql_delete=value['sql_delete']
            self.relaton.delete_sql(sql_delete)



            if self.duanyan.panduan(expect_sql, res):
                self.data.write_Result(int(value['id']),'pass')
                pass_count.append(int(value['id']))
            else:
                self.data.write_Result(int(value['id']), 'fail')
                fail_count.append(int(value['id']))

    def tearDown(self):
        loging.info('测试结束')

if __name__ == "__main__":
    unittest.main()
