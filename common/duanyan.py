# coning = utf-8
#-*- coding: UTF-8 -*-
__author__ = 'Aimee'
import json
# from selenium import webdriver
from jsonpath_rw import jsonpath,parse
class DuanYan():
    def is_contain(self,str_one,str_two):
        #判断一个字符串是否在另一个字符串中
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def panduan(self,expect,res):
        expect_left = []
        expect_value = []
        res_value = []
        for i in str(expect).split(';'):
            expect_left.append(i.split('=')[0])
            expect_value.append(i.split('=')[1].strip('\n'))

        for i in expect_left:
            json_exe = parse(i)
            madle = json_exe.find(res)
            x = [math.value for math in madle][0]
            if isinstance(x, int) or x == None:
                x = str(x)
            res_value.append(x)

        flag = None
        if expect_value == res_value:
            flag = True
        else:
            flag = False
        return flag


if __name__ == '__main__':
    x = DuanYan()
    expect = 'code=200;status=true;msg=None;info.recommendProjectList[1].id=219'
    res = {'status': 'true', 'msg': None, 'info': {'project': {'detailPic': 'https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111156596hk2.jpg', 'statusName': '启用', 'effectiveStart': None, 'reportBrief': None, 'shareIcon': None, 'detailPics': None, 'claimedAt': None, 'certificateModelPic': '1', 'reportContent': None, 'areaNames': None, 'createAt': '2018-05-24 18:37:50', 'status': 20, 'name': '毕业后公益图书室', 'updateAt': '2018-06-01 12:12:11', 'viewCount': 3558, 'keyWord': None, 'target': None, 'relOrg': None, 'type': None, 'sort': 0, 'reportedAt': None, 'address': None, 'deleted': 0, 'relCat': 1, 'id': 213, 'city': None, 'open': True, 'recipient': None, 'countPerson': 11336, 'district': None, 'shareDetail': None, 'certificateBgs': None, 'effectiveEnd': None, 'province': None, 'shareTitle': None, 'relUser': None, 'countMoney': 179837, 'areaIds': None, 'detailContent': '<p><img src="https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111358297mPv.jpg"></p><p><br></p><p><span style="color: rgb(57, 57, 57);">【乡村阅读面临严峻挑战】</span></p><p><span style="color: rgb(57, 57, 57);">走进图书馆看书、借书，对不少城市儿童来说并非难事，他们可以</span><span style="color: rgb(51, 51, 51);">轻松看到琳琅满目的儿童读物，</span><span style="color: rgb(57, 57, 57);">但对于资源缺乏的农村地区孩子来说，却是一种奢望，</span><span style="color: rgb(51, 51, 51);">是一个可望而不可即的梦想</span><span style="color: rgb(57, 57, 57);">。毕业后公益图书室在贫困地区建立公益图书室的学校中，一所拥有300多名学校的乡村学校中，竟然找不到一本课外读物，乃至经济发达的珠三角地区依然有多个学校存在此现象。这些乡村学校，图书室就像是一个被遗忘的角落。</span></p><p><span style="color: rgb(57, 57, 57);">据《中国留守儿童心灵状况白皮书》（2015）显示，我国的城镇儿童拥有着童书资源的88.9%，农村儿童仅拥有11.1%。</span><span style="color: rgb(51, 51, 51);">这也说明，目前我国存在着严重的农村儿童“阅读缺失”的情况。</span></p><p><br></p><p><img src="https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111437037cPL.jpg"></p><p><br></p><p><img src="https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111441097E4t.jpg"></p><p><br></p><p><span style="color: rgb(57, 57, 57);">【振兴乡村阅读计划】</span></p><p><span style="color: rgb(57, 57, 57);">成长环境的差距，教育资源的匮乏，与薄弱的教育基础共同构成了贫困地区全面阅读难以克服的瓶颈，让孩子们失去更多发展的可能。为了改善乡村学生阅读环境，缩小与城里孩子的距离，一群全国各地在校的大学生发起了“毕业后公益图书室”公益项目，开展振兴乡村阅读计划，为孩子们架起一道了解外面世界的桥梁，帮助他们拥有更多人生选择性。让书有人看，让人有书看，让书成为一种力量。</span></p><p><br></p><p><img src="https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111514101pXv.jpg"></p><p><br></p><p><span style="color: rgb(57, 57, 57);">【毕业后公益图书室介绍】</span></p><p><span style="color: rgb(57, 57, 57);">毕业后公益图书室是由广州大学刘楠鑫联合国内外500多名有影响力大学生发起，号召中国 4000 万在校大学生作为主人公投身公益实践，募集精准闲置书籍，向边远山区农村、城镇中小学等场所搭建公益图书室，让书有人看，让人有书看，在此基础上流转公益图书室，实现循环使用直至废品，让闲置图书不再是0价值物品，通过公益手段赋予能量，放大闲置书籍价值，让书成为一种力量。并组建大学生以图书室为桥梁开展真人图书馆、阅读推广等活动运营图书室，以此感召更多的社会人士参与，同时让参与者在公益实践的过程中不断成长，并提高道德修养和提升人格魅力。</span></p><p><br></p><p><img src="https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111548077KJ4.jpg"></p><p><br></p><p><img src="https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111608882MgT.jpg"></p><p><br></p><p>【噢啦公益图书室冠名计划】</p><p>毕业后公益图书室与噢啦目前正在开展“为爱而捐，与噢啦同行”百所高校以废代捐大型公益活动。我们将联动全国各高校社团、明星粉丝团及社会力量，通过“环保+公益”的社会创新模式，举办“以废代捐”公益活动。与此同时，高校活动将为大学生提供低门槛公益参与方式，号召大学生通过噢啦OOLA互联网平台捐献身边闲置物品，减少资源浪费。通过环保回收可获得噢啦豆奖励，噢啦豆通过雷猴公益促进基金会折换成善款全部用于公益图书室的建设，同时冠名“噢啦公益图书室”，来帮助留守儿童拥有更多人生选择性。</p><p><br></p><p><img src="https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111633406y3D.jpg"></p><p><br></p><p><img src="https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111709977DDZ.jpg"></p><p><br></p><p><img src="https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/20180525111712350w9w.jpg"></p>', 'certificateCopy': None, 'detailIntro': '“为爱而捐，与噢啦同行”百所高校以废代捐大型公益活动由噢啦OOLA与毕业后公益图书室联合发起，联动高校社团通过“环保+公益”的社会创新模式，举办“以废代捐”公益活动，为大学生提供低门槛公益参与方式，号召大学生通过噢啦OOLA互联网平台捐献身边闲置物品，减少资源浪费。同时环保回收产生的经济价值将用于国内边远山区公益图书室搭建，帮助留守儿童拥有更多人生选择性。以此感召更多社会力量参与，以废代捐，做新时代指尖环保公益行动者，推动公益事业的发展。', 'originateOrg': 68}, 'projectOrderToken': 'acf434d09f974bd1a1b9ab0fe8fb0399', 'recommendProjectList': [{'detailPic': 'https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180802/20180802181144783P9f.jpg', 'name': '以爱童行', 'id': 222, 'relOrg': None, 'sort': None, 'countPerson': 41, 'detailIntro': '为当地困境中的少年儿童提供圆梦红包，实现他们小小的心愿。', 'originateOrg': 74, 'createAt': '2018-08-02 18:16:15'}, {'detailPic': 'https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180706/20180706095937378zTM.jpg', 'name': '憨福儿就业支持计划', 'id': 219, 'relOrg': None, 'sort': None, 'countPerson': 9335, 'detailIntro': '“我想要工作，我不想啃老”——本项目为16岁以上的心智障碍者提供彩绘、烘焙工作技能训练以及基本职业素质能力教育，帮助憨福儿们学会一门技能，用自己的双手养活自己，在工作中实现职业康复！', 'originateOrg': 71, 'createAt': '2018-07-06 10:06:35'}, {'detailPic': 'https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180514/201805141522591765K2.jpg', 'name': '爱笑流浪猫狗救助', 'id': 212, 'relOrg': None, 'sort': None, 'countPerson': 46778, 'detailIntro': '通过领养等方式使基地里动物的生存福利得到合理提高', 'originateOrg': 67, 'createAt': '2018-05-14 15:36:49'}], 'cooperateInstitution': None, 'originateInstitution': {'name': '广东天添向尚网络科技股份有限公司', 'intro': '软件和信息技术服务业', 'id': 68, 'homepage': None, 'imgLogo': 'https://oola-oss.oss-cn-shenzhen.aliyuncs.com/oola-oss/imgs/20180525/2018052510570583224Y.jpg'}}, 'code': '200'}
    # y = x.panduan(expect,res)
    # print(y)


    # expect ={'info.credit': '18865', 'status': 'true', 'code': '200'}

    # res ={'info': {'weixinNickname': None, 'bindWeixin': 0, 'credit': 18952, 'weiboNickName': None, 'headImgUrl': 'https://images-w.oola.cn/oola-web/imgs/20190228/20190228181329029ePS.png', 'bindQQ': 0, 'data': None, 'nickname': 'Aimeepinfhhd', 'telephone': '13527231857', 'socialAccountId': None, 'smallProgramData': None, 'username': '13527231857', 'qqNickName': None, 'id': 162064, 'bindWeibo': 0, 'avatar': 'https://images-w.oola.cn/oola-web/imgs/20190228/20190228181329029ePS.png', 'avatarUrl': None, 'avatarS': None}, 'status': 'true', 'msg': None, 'code': '200'}
    expect_left = []
    expect_value = []
    res_value = []
    for i in str(expect).split(';'):
        print(i)

        expect_left.append(i.split('=')[0])
        print(expect_left.append(i.split('=')[0]))
        # expect_value.append(i.split('=')[1].strip('\n'))



    # y = x.panduan(expect_sql, res)
    # print(y)
