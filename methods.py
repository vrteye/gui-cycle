import re
import json
import time
import random
import urllib
import codecs
import hashlib
import os, pprint
import urllib.parse, urllib.request

def TranslateBaidu(text, f='zh', t='en'):
    try:
        # 百度二次翻译，中-英-中
        appid = '20201014000589123'
        secretKey = '_Yfh1lzTWPDXytFhfYr2'
        url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        salt = random.randint(32768, 65536)
        sign = appid + text + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        url = url_baidu + '?appid=' + appid + '&q=' + urllib.parse.quote(text) + '&from=' + 'zh' + '&to=' + 'en' + '&salt=' + str(
            salt) + '&sign=' + sign
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        data = json.loads(content)
        result = str(data["trans_result"][0]['dst'])
        time.sleep(1)   # 时间
        # 第二次翻译
        appid = '20201016000590625'
        secretKey = 'TW8AeSIyRwEeeIr5RSN4'
        url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        salt = random.randint(32768, 65536)
        sign = appid + result + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        url = url_baidu + '?appid=' + appid + '&q=' + urllib.parse.quote(
            result) + '&from=' + 'en' + '&to=' + 'zh' + '&salt=' + str(
            salt) + '&sign=' + sign
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        data = json.loads(content)
        result = str(data["trans_result"][0]['dst'])
        return result
    except:
        pass

def File_List(url):
    # 提供全链接，去除文本中的换行符;结果返回一个列表，每个段落装在字符串,整体装在列表，打印出来。
    file = open(url, encoding='utf-8')
    file = list(file)
    file = [x for x in file if x != '\n']
    # 如果要装在字符串中
    # str_file = ''.join(file)
    return file
# F = File_List('/Volumes/U盘/test/2.txt')
# print(F[2])
def Txt_Create(Target_Path,name, msg):
    # 新创建的txt文件的存放路径,需要提供url,生成文本及内容。msg是str。
    full_path = Target_Path + name + '.txt'  # 也可以创建一个.doc的word文档
    # Target_Path='/Volumes/U盘/test/'
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world
    file.close()
    return file

def File_Eli(path):
    # 剔除隐藏的文件,需要提供被测文件的路径，生成一个剔除隐藏文件后的列表。
    # path = '/Volumes/U盘/test/'
    path = os.listdir(path)
    ls = []
    for f in path:
        # print(f)
        if not f.startswith('.'):
            ls.append(f)
    return ls

def Read_File(Path,ls):
    # 提供path(路径)和ls(剔除隐藏文件的的列表)，能打印出列表文本中的内容
    # print("#"+Path,ls)
    file_content = []
    for i in range(len(ls)):
        url = Path + ls[i]
        f = open(url, encoding="utf-8")
        f = list(f)
        file_content.append(f)
    return file_content

# 生成文件夹
def Make_Folers(Target_Path,Dir_Name):
    # all_link = '/Users/lilong/Desktop/in/{}'.format(dir_name)
    # /Users/lilong/Desktop/
    Target_Link = Target_Path + Dir_Name
    Dir = os.makedirs(Target_Link)
    return Dir