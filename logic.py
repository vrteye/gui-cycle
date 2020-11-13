import random
from methods import *
from toutiao import *
# 建立映射关系储存到变量，生成列表
# url地址
url_zm_toutiao = 'TW/ZM/zm_toutiao/zm_toutiao_test.txt'     # 头条地址
url_zm_weibo = 'TW/ZM/zm_weibo/zm_weibo_test.txt'       # 微博地址
url_tc_toutiao = 'TW/TC/tc_toutiao/test/'     # 头条文件夹
url_tc_weibo = 'TW/TC/tc_weibo/test/'     # 微博文件夹

# aa = File_Eli(url_tc_toutiao)
# print(aa)
# bb = File_Eli(url_tc_weibo)
# print(bb)

Select = int(input("输入0是头条，其他是微博："))
num = int(input("请输入循环次数："))
for j in range(num):
    knum = j+1
    if Select == 0:     # 头条文本以及文件夹下内容
        print("【你的选择是头条，第{0}轮循环】".format(knum))
        T_Content_filename = File_Eli(url_tc_toutiao)
        random.shuffle(T_Content_filename)      # 随机打乱列表内容
        T_Content_name = [i.replace('.txt', '') for i in T_Content_filename]        # 去除.txt
        # print('这是头条内容标题：', T_Content_name)
        f_zm_toutiao = open(url_zm_toutiao, encoding='utf-8')
        list_f_zm_toutiao = list(f_zm_toutiao)
        T_2d = []
        for i in list_f_zm_toutiao:
            Replace = i.replace('\n', '')
            Split = Replace.split(',')
            T_2d.append(Split)

        k = 0
        for i,T_Con in zip(T_2d,T_Content_filename):
            k += 1
            T_Con_name = T_Con.replace('.txt', '')
            url = url_tc_toutiao + T_Con
            T_Conttent = File_List(url)
            str_T_Con = ''.join(T_Conttent)
            print('第{0}个账号密码'.format(k))
            zh = [i][0][0]
            ma = [i][0][1]
            print('账号：', zh, '密码：', ma, '标题：', T_Con_name, '内容：', str_T_Con)

    else:
        print("【你的选择是微博，第{0}轮循环】".format(knum))
        W_Content_filename = File_Eli(url_tc_weibo)
        random.shuffle(W_Content_filename)      # 随机打乱列表内容
        W_Content_name = [i.replace('.txt', '') for i in W_Content_filename]

        # print('这是微博标题：', W_Content_name)
        f_zm_weibo = open(url_zm_weibo, encoding='utf-8')
        list_f_zm_weibo = list(f_zm_weibo)
        W_2d = []
        for i in list_f_zm_weibo:
            Replace = i.replace('\n', '')
            Split = Replace.split(',')
            W_2d.append(Split)
        # print("微博账号密码：",W_2d)
        k = 0
        for i,W_Con in zip(W_2d,W_Content_filename):
            k += 1
            url = url_tc_weibo + W_Con      # 路径

            W_Conttent = File_List(url)     # 打开路径下文本，获取内容
            str_W_Con = ''.join(W_Conttent)     # 由列表转为字符串
            print('第{0}个账号密码'.format(k))
            # print(i)
            # print(W_2d)
            zh = [i][0][0]  # 账号
            ma = [i][0][1]  # 密码
            # print('账号：', zh, '密码：', ma, '内容：', str_W_Con)
