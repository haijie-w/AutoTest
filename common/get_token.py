# coning = utf-8
__author__ = 'Aimee'
import json
import requests
from common.operation_json import OperationJson

class GetToken():
    def __init__(self,response):
        self.response = response
    def get_response_token(self):
        Token = self.response['info']
        return Token
    def write_token(self):
        token = self.get_response_token()
        op_json = OperationJson()
        op_json.write_data(token)

if __name__ == '__main__':

    url = 'https://uat.oola.cn/oola-api/app/base/user/loginByCode'
    data = {"telephone":" 13527231857","verifyCode":"123456"}
    res = requests.post(url,data=data)
    res = res.json()

    token = GetToken(res)

    token.write_token()



