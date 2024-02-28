# Remaining-reminders-of-the-art-course
在程序的开始配置一下账号信息后就可以挂载到服务器了
## 超级鹰
超级鹰(验证码识别平台)官网:https://www.chaojiying.com/
注册完绑定微信送1000分，10分一次也够用了，软件id在用户中心最下面需要自己创建
程序设定了题分不够会提醒你补分
## bark软件
在苹果AppStore下载软件(安卓我不清楚有没有)bark,之后选取第二栏里面`api.day.app/`后面的一串字符填进去就可以了
## 邮箱发送服务
这个功能需要发送的邮箱开通SMTP/POP3服务，不同公司的邮箱开通方法可能不一样，请自行百度
## 服务器环境配置
服务器的环境配置详见这篇
https://github.com/password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian
需要配置的有python3,selenium,requests,webdriver-manager等
## 启动
最后直接Python3启动就行了,程序默认是半小时查询一次，可以在代码最后一行sleep(1800)自行修改
