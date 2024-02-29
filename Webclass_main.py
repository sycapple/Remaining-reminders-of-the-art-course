import time

from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import requests
from hashlib import md5

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from config import *


def sender(title, content):
    global send_method
    ret = True
    try:
        if send_method == 0:
            msg = MIMEText(content, 'plain', 'utf-8')  # 填写邮件内容
            msg['From'] = formataddr(["tracy", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["test", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = title  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        elif send_method == 1:
            requests.get(f"https://api.day.app/{bark_api}/{title}/{content}")
        elif send_method == 2:
            msg = MIMEText(content, 'plain', 'utf-8')  # 填写邮件内容
            msg['From'] = formataddr(["tracy", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["test", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = title  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            requests.get(f"https://api.day.app/{bark_api}/{title}/{content}")
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64': base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


def red(text):
    return '\033[31m{}\033[0m'.format(text)


def yellow(text):
    return '\x1b[33m{}\x1b[0m'.format(text)


def blue(text):
    return '\x1b[36m{}\x1b[0m'.format(text)


def current_time():
    return yellow(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


if __name__ == '__main__':
    while True:
        print(f"[INFO]|{current_time()}|欢迎来到课程搜集系统")
        print(f"[INFO]|{current_time()}|正在准备程序")

        # 创建浏览器对象
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        web = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        web.execute_cdp_cmd("Emulation.setUserAgentOverride", {
            "userAgent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
        })
        if WebVpn_Flag:
            web.get('https://webvpn.bit.edu.cn/')
            print(f"[INFO]|{current_time()}|登录一体化认证")
            print(f"[INFO]|{current_time()}|进入选课网站")
            web.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys(ACCOUNT)
            web.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(PASSWORD, Keys.ENTER)
            time.sleep(1)
            web.find_element(by=By.XPATH, value='//*[@id="group-8"]/div[2]/div').click()
            web.switch_to.window(web.window_handles[-1])
        else:
            web.get('https://xk.bit.edu.cn/xsxkapp/sys/xsxkapp/*default/index.do')
        print(f"[INFO]|{current_time()}|当前登录信息如下")
        print(f"[INFO]|{current_time()}|用户:{blue(ACCOUNT)}")
        print(f"[INFO]|{current_time()}|密码:{blue(PASSWORD)}")
        web.find_element(by=By.XPATH, value='//*[@id="loginName"]').send_keys(ACCOUNT)
        web.find_element(by=By.XPATH, value='//*[@id="loginPwd"]').send_keys(PASSWORD)
        pic_id = None
        while True:
            try:
                web.find_element(by=By.XPATH, value='//*[@id="buttons"]/button[2]')
                break
            except exceptions.NoSuchElementException as e:
                img = web.find_element(by=By.XPATH, value='//*[@id="vcodeImg"]').screenshot_as_png
                chaojiying = Chaojiying_Client(verify_code_ACCOUNT, verify_code_PASSWORD, soft_id)
                if pic_id:
                    print(f"[INFO]|{current_time()}|验证码{blue(verify_code)}错误")
                    chaojiying.ReportError(pic_id)
                dic = chaojiying.PostPic(img, 1902)
                pic_id = dic['pic_id']
                if dic['err_no'] == 1005:
                    sender('题分不足', '题分不足')
                    print(f"[INFO]|{current_time()}|题分不足")
                    exit()
                verify_code = dic['pic_str']
                print(f"[INFO]|{current_time()}|尝试验证码{blue(verify_code)}")
                web.find_element(by=By.XPATH, value='//*[@id="verifyCode"]').send_keys(verify_code, Keys.ENTER)
                time.sleep(0.5)
        try:
            web.find_element(by=By.XPATH, value='//*[@id="buttons"]/button[2]').click()
        except exceptions.NoSuchElementException as e:
            pass
        web.find_element(by=By.XPATH, value='//*[@id="courseBtn"]').click()

        web.find_element(by=By.XPATH, value='//*[@id="aPublicCourse"]').click()
        web.find_element(by=By.XPATH, value='//*[@id="public_sfct"]/option[3]').click()
        web.find_element(by=By.XPATH, value='//*[@id="public_sfym"]/option[3]').click()
        web.find_element(by=By.XPATH, value=f'//*[@id="public_xgxklb"]/option[{Class_Subject + 1}]').click()
        web.find_element(by=By.XPATH, value='//*[@id="publicSearch"]').send_keys(className, Keys.ENTER)
        time.sleep(1)
        total_page = eval(web.find_element(by=By.XPATH, value='//*[@id="publicTotalPage"]').text)
        now_page = eval(web.find_element(by=By.XPATH, value='//*[@id="publicPageNumber"]').text)
        class_names = []
        if total_page == 0:
            sender("课程提醒", "当前无课程")
            class_names.append("当前无课程")
        else:
            while now_page <= total_page:
                divs = web.find_elements(by=By.XPATH, value='//*[@id="publicBody"]/div')
                for div in divs:
                    try:
                        class_name = div.text
                        class_name = class_name.split('\n')[3]
                        if Auto_select == True:
                            web.find_element(by=By.XPATH, value='/div[11]/a').click()
                            web.find_element(by=By.XPATH, value='//*[@id="cvDialog"]/div[2]/div[2]/div[1]').click()
                            print(f"[INFO]|{current_time()}|已选择 {blue(class_name)}")
                            sender(f"课程提醒", f"已选择{class_name}")
                            exit()
                        class_names.append(class_name)
                    except:
                        pass
                web.find_element(by=By.XPATH, value='//*[@id="publicDown"]').click()
                now_page += 1
            sender(f"课程提醒", f"{' '.join(class_names)}")
        print(f"[INFO]|{current_time()}|已推送 {blue(' '.join(class_names))}")
        web.quit()
        time.sleep(Push_cycle)
