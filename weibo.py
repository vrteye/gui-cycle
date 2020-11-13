import time
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# while True:
    # text = input("请输入内容：")
def weibo(Account,Password,Content):
    def slip_verify():
        iframe = driver.find_element_by_xpath('//iframe')
        driver.switch_to_frame('iframe')
        span_background = driver.find_element_by_id('slide')
        span_background_size = span_background
        print(span_background_size)
        # 获取滑块位置
        button = driver.find_element_by_id('tcaptcha_drag_button')
        return
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
    driver_path = "/Users/lilong/Desktop/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('http://www.weibo.com/login.php')
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[5]/div/a[1]').click()    # 微博上的QQ图标，点击qq图标
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.frame('ptlogin_iframe') # 登录表单在页面框架中，所以要切换到该框架
    driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()  # 账号密码登录
    while driver.title == 'QQ帐号安全登录':
        if is_element_exist('tcaptcha_drag_button'):
            slip_verify()
        else:
            print("输入账号密码登录")
            try:
                driver.find_element_by_xpath('//*[@id="u"]').send_keys(Account)
                driver.find_element_by_xpath('//*[@id="p"]').send_keys(Password)
                driver.find_element_by_xpath('//*[@id="login_button"]').click()
                time.sleep(5)
                driver.switch_to_default_content()

                driver.find_element_by_css_selector('textarea.W_input').send_keys(Content)   # 将获取的内容输入文字框
                time.sleep(2)
                driver.find_element_by_css_selector('a.W_btn_a:nth-child(2)').click()   # 点击发布按钮
                print("ok")
            except:
                print("再来！")
                pass



