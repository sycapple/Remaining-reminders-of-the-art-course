# 材料准备
本项目是基于`selenium4`的一个爬虫项目，旨在帮助没能抽中艺术课等自己心仪课程的同学一个再次选择的机会，想要自己部署这个项目，你需要以下材料
1. 一台Linux云端服务器，或者保持自己的电脑24h开机
2. Bark消息接受App Or 一个拥有POP3/SMTP服务的邮箱账号
# 搭建流程
## 1. 安装Python
这个挺小白的，这边给出一个csdn的教程
### 1.1 Windows安装
[Windows 系统上如何安装 Python 环境（详细教程）python环境安装-CSDN博客](https://blog.csdn.net/qq_44214671/article/details/113469811)
### 1.2 Linux安装
[Linux系统上安装python详细步骤_linux 安装python-CSDN博客](https://blog.csdn.net/weixin_39447365/article/details/121159894)
## 2 环境搭建
### 2.1 Windows环境搭建
1. 双击项目中的`set-up.bat`即可完成Python环境的搭建
2. 在浏览器上下载Chome浏览器(必须要Chrome)，自行安装
### 2.2 Linux环境搭建
1. 在项目文件目录下执行`pip install -r requirements.txt`完成python环境的搭建
2. 参照这个链接完成剩余环境的搭建[password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian: Setup Selenium and Chrome driver on ubuntu/debian (github.com)](https://github.com/password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian)
# 3. 配置超级鹰
1. 首先进入超级鹰官网([超级鹰验证码识别-专业的验证码云端识别服务,让验证码识别更快速、更准确、更强大 (chaojiying.com)](https://www.chaojiying.com/))，自己注册一个账号
2. 进入用户中心，下拉选择左侧的软件ID，点击生成一个软件ID，表单随便填写，生成以后记录软件ID
3. 充值题分的话，绑定公众号送1000分够用了，绑不上就冲1￥，也够用了
## 4. 项目运行
在项目中有多个有用文件，他们的用途如下

| 文件名              | 用途                   |
| ---------------- | -------------------- |
| main.py          | 预置选项为不冲突、未满、艺术与文学    |
| Webclass_main.py | 预置选项为不冲突、未满，且支持课程预搜索 |

