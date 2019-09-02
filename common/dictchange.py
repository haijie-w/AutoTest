# coning = utf-8
__author__ = 'Aimee'

"""本程序主要是将超长的request_Body快速转化成dict格式"""

str = input("请输入你要转化的RequestBody:")
strlen = len(str.split("&"))
print(strlen)
DictNum1List = []
DictNum2List = []
DictBody = {}
for i in range(0, strlen):
    try:
        DictNum1 = str.split("&")[i].split("=")[0]
        DictNum2 = str.split("&")[i].split("=")[1]
        DictNum1List.append(DictNum1)
        DictNum2List.append(DictNum2)
    except Exception as Ex:
        print("非RequestsBody格式，请重新输入....")
        exit(0)

for x in range(0, len(DictNum1List)):
    DictBody[DictNum1List[x]] = DictNum2List[x]

print("转化的dict格式如下，直接复制使用即可：")
print(DictBody)

