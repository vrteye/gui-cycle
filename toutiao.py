import time
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def toutiao(Account,Password,Title,Content):
    def is_element_exist(css):
        s = driver.find_elements_by_css_selector(css_selector=css)
        if len(s) == 0:
            # print("元素未找到：%s"%css)
            pass
            # return False
        elif len(s) == 1:
            return True
        else:
            # print("找到%s个元素：%s"%(len(s),css))
            pass
            # return False


    def is_element_xpath(xpth):
        try:
            if driver.find_element_by_xpath(xpth).text == '确定':

                print('已经超过3次发文')
                driver.find_element_by_xpath(xpth).click()
            else:
                pass
        except:
            pass


    def slip_verify():
        iframe = driver.find_element_by_xpath('//iframe')
        driver.switch_to_frame('iframe')
        span_background = driver.find_element_by_id('slide')
        span_background_size = span_background
        print(span_background_size)
        # 获取滑块位置
        button = driver.find_element_by_id('tcaptcha_drag_button')
        return
    while True:
        driver_path = "/Users/lilong/Desktop/chromedriver"
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get('https://mp.toutiao.com')
        driver.find_element_by_xpath('//*[@id="login-root"]/div[2]/div[4]/div[2]/a').click()
        driver.find_element_by_xpath('//*[@id="sso_qzone_sns"]/span').click()
        driver.implicitly_wait(5) # 隐性等待，最长等5秒
        driver.switch_to.frame('ptlogin_iframe') # 登录表单在页面框架中，所以要切换到该框架
        driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()  # 账号密码登录
        try:
            driver_path = "/Users/lilong/Desktop/chromedriver"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get('https://mp.toutiao.com')
            driver.find_element_by_xpath('//*[@id="login-root"]/div[2]/div[4]/div[2]/a').click()
            driver.find_element_by_xpath('//*[@id="sso_qzone_sns"]/span').click()
            driver.implicitly_wait(5)  # 隐性等待，最长等5秒
            driver.switch_to.frame('ptlogin_iframe')  # 登录表单在页面框架中，所以要切换到该框架
            driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()  # 账号密码登录
            while driver.title == 'QQ帐号安全登录':
                if is_element_exist('tcaptcha_drag_button'):
                    slip_verify()
                else:
                    print("输入账号密码登录")
                    driver.find_element_by_xpath('//*[@id="u"]').send_keys(Account)
                    driver.find_element_by_xpath('//*[@id="p"]').send_keys(Password)
                    driver.find_element_by_xpath('//*[@id="login_button"]').click()
                    time.sleep(5)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/aside/div/div/div/div[2]/div[2]/div[1]/span/a').click()  # 点击文章
                    driver.implicitly_wait(5)
                    # if is_element_exist('byte-modal-title'):
                    is_element_xpath('/html/body/div[19]/div[2]/div/div[3]/div[3]/button/span')  # 3次发文限制函数
                    driver.implicitly_wait(5)
                    driver.find_element_by_xpath('/html/body/div[3]/div[1]').click()  # 点击空白处，关闭发文助手
                    driver.implicitly_wait(3)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div/textarea').send_keys(Title)  # 输入标题
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[1]/div[4]/div/div[1]/p[1]').send_keys(Content)  # 输入内容
                    # driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[1]/div[4]/div/div[1]/p[1]').click()  # 点击标题
                    driver.implicitly_wait(5)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[1]/div[1]/div/div[15]/div/button').click()  # 点击图片
                    driver.implicitly_wait(5)
                    driver.find_elements_by_class_name('new-li')[1].click()  # 智能配图

                    try:
                        print("方案一")
                        driver.find_elements_by_class_name(
                            'byte-btn byte-btn-default byte-btn-size-large byte-btn-shape-square publish-btn')[1].click()
                    except:
                        pass
                    time.sleep(1)
                    try:
                        print("方案二")
                        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[3]/div/button[4]/span').click()
                    except:
                        pass
        except:
            print("再次登陆")
            driver_path = "/Users/lilong/Desktop/chromedriver"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get('https://mp.toutiao.com')
            driver.find_element_by_xpath('//*[@id="login-root"]/div[2]/div[4]/div[2]/a').click()
            driver.find_element_by_xpath('//*[@id="sso_qzone_sns"]/span').click()
            driver.implicitly_wait(5)  # 隐性等待，最长等5秒
            driver.switch_to.frame('ptlogin_iframe')  # 登录表单在页面框架中，所以要切换到该框架
            driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()  # 账号密码登录
            while driver.title == 'QQ帐号安全登录':
                if is_element_exist('tcaptcha_drag_button'):
                    slip_verify()
                else:
                    print("输入账号密码登录")
                    driver.find_element_by_xpath('//*[@id="u"]').send_keys(Account)
                    driver.find_element_by_xpath('//*[@id="p"]').send_keys(Password)
                    driver.find_element_by_xpath('//*[@id="login_button"]').click()
                    time.sleep(5)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/aside/div/div/div/div[2]/div[2]/div[1]/span/a').click()  # 点击文章
                    driver.implicitly_wait(5)
                    # if is_element_exist('byte-modal-title'):
                    is_element_xpath('/html/body/div[19]/div[2]/div/div[3]/div[3]/button/span')     # 3次发文限制函数
                    driver.implicitly_wait(5)
                    driver.find_element_by_xpath('/html/body/div[3]/div[1]').click()    # 点击空白处，关闭发文助手
                    driver.implicitly_wait(3)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div/div/div/textarea').send_keys(Title)     # 输入标题
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[1]/div[4]/div/div[1]/p[1]').send_keys(Content)       # 输入内容
                    # driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[1]/div[4]/div/div[1]/p[1]').click()  # 点击标题
                    driver.implicitly_wait(5)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[1]/div[1]/div/div[15]/div/button').click()     # 点击图片
                    driver.implicitly_wait(5)
                    driver.find_elements_by_class_name('new-li')[1].click()     # 智能配图

                    try:
                        print("方案一")
                        driver.find_elements_by_class_name('byte-btn byte-btn-default byte-btn-size-large byte-btn-shape-square publish-btn')[1].click()
                    except:
                        pass
                    time.sleep(1)
                    try:
                        print("方案二")
                        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/section/main/div[2]/div/div/div[3]/div/button[4]/span').click()
                    except:
                        pass