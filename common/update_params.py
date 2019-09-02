# coning = utf-8
__author__ = 'Aimee'


def update_params(value,relation_dict):
    param = value['params']
    if param == '':
        data = None
    else:
        data = eval(param)

        if relation_dict != None:
            for item in range(len(relation_dict)):
                if str(data).find(list(relation_dict.keys())[item]) != -1:
                    data = eval(str(data).replace(list(relation_dict.keys())[item], list(relation_dict.values())[item]))
                else:
                    data = data
        return data



