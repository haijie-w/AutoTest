# coning = utf-8
__author__ = 'Aimee'
import os,time
from config.readConfig import ReadConfig
now = time.strftime('%Y-%m-%d')
#项目路径
project_path = os.path.abspath(os.path.join(os.getcwd(), ".."))


#log
log_path = os.path.join(project_path,r'logs',now+'.log')

#测试数据路径
data_path = os.path.join(project_path,r'test_data','TestCase_OOLA_APP.xls')
#报告位置
report_path = os.path.join(project_path,'result','TestReport' + now + '.html')

#case位置
case_path = os.path.join(project_path,'test_case')


#
# print (os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# print (os.path.abspath(os.path.dirname(os.getcwd())))
# print (os.path.abspath(os.path.join(os.getcwd(), "..")))
#
#
# print (os.path.abspath(os.path.join(os.getcwd(), "../..")))
