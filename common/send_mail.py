# coning = utf-8
__author__ = 'Aimee'
from config.readConfig import ReadConfig
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from config.project_path import report_path,data_path,log_path
from common.loger import Log

log = Log()
now_time =time.strftime('%Y-%m-%d %H:%M:%S')
#获取配置信息
info = ReadConfig()
email_host=info.get_email('mail_host')
send_user=info.get_email('mail_send')
password=info.get_email('mail_sender_password')
sub = info.get_email('subject')
user = "Aimee"+"<"+send_user+">"
receivers=info.get_email('receiver').split(';')
filepath=[report_path,data_path,log_path]


class sendEmail():
    def send_mail(self,receivers , filepath):
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ','.join(receivers)

        #邮件正文
        part = MIMEText(content,_subtype='plain',_charset='utf-8')
        message.attach(part)

        #附件 filepath 是一个列表
        for path in filepath:
            if ".xls" in path:
                #xlsx类型附件
                part = MIMEText(open(path,'rb').read(), 'base64', 'utf-8')
                xls_name = path.split("\\")[-1]
                # part["Content-Type"] = 'application/octet-stream'
                # part["Content-Disposition"] = 'attachment; filename='xls_name''
                part.add_header('Content-Disposition', 'attachment', filename=xls_name)
                message.attach(part)

            if ".html" in path:
                #html类型附件
                part = MIMEText(open(path,'rb').read(), 'base64', 'utf-8')
                html_name = path.split("\\")[-1]
                # part["Content-Type"] = 'application/octet-stream'
                # part["Content-Disposition"] = 'attachment; filename="html_name"'
                part.add_header('Content-Disposition', 'attachment', filename=html_name)
                message.attach(part)

            if ".xml" in path:
                #xml类型附件
                part = MIMEText(open(path,'rb').read(), 'base64', 'utf-8')
                xml_name = path.split("\\")[-1]
                part.add_header('Content-Disposition', 'attachment', filename=xml_name)
                message.attach(part)

            if ".log" in path:
                #log类型附件
                part = MIMEText(open(path,'rb').read(), 'base64', 'utf-8')
                log_name = path.split("\\")[-1]
                part.add_header('Content-Disposition', 'attachment', filename=log_name)
                message.attach(part)
        try:
            server = smtplib.SMTP()
            server.connect(email_host)
            server.login(send_user,password)
            server.sendmail(user,receivers,message.as_string())
            server.close()
            log.info("邮件发送成功")
        except Exception as e:
            log.error("邮件发送失败 出错是:%s" %e)


    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        # 90%  %%表示百分号
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        global content
        content = "%s 此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s,详情请见附件" % (now_time,count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(receivers,filepath)

if __name__ == "__main__":
    s = sendEmail()
    # receivers = "aimee_h@gzleihou.cn,974325839@qq.com"
    # filepath = ['C:\\auto_API_cases\common\Result\html_report\TestReport2018-09-06_14_07_27.html','C:\\auto_API_cases\common\Result\log\\test_log.txt']
    # pass_list = [1,2,3,4]
    # fail_list = [5,6,7,8,9,10]
    #
    # y = s.send_main(pass_list,fail_list)
