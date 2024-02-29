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

## 4. 推送配置

### 4.1 Bark推送

1. 在App Store搜索红色图标的Bark下载
2. 进入bark主页后记录以下字符串中的`BarkApi`
   `https://api.day.app/<awdadawdAIDMdaiF这个尖括号里面的文字>/推送标题/这里改成你自己的推送内容`

### 4.2 邮箱开启服务

1. 以qq邮箱为例，进入网页版qq邮箱后，点击右上角`账号与安全`
2. 左侧点击安全设置向下拉，按照流程开启POP3/IMAP/SMTP/Exchange/CardDAV 服务
3. 系统会给你一个授权码，记下来，后面就看不了了

## 5. 项目配置

在项目`config.py`中有以下几个配置需要填写

* `ACCOUNT`: 校园网账号，必填
* `PASSWORD`：校园网密码，必填
* `verify_code_ACCOUNT`：超级鹰账号，必填
* `verify_code_PASSWORD`：超级鹰密码，必填
* `soft_id`：超级鹰软件ID，必填
* `send_method`：推送方式，必填
* `my_sender`：发信人，选填
* `my_pass`：邮箱授权码，选填
* `my_user`：收件人邮箱，选填
* `bark_api`：barkapi，选填
* `className`：预检索名称，选填
* `Push_cycle`：推送间隔，必填
* `Class_Subject`：公选课类别，选填
* `WebVpn_Flag`：是否校外访问
* `Auto_select`：是否自动选课(慎重选择，否则满足条件的都给你选上了)
* `Dev_Mode`:调试模式

## 6. 项目运行

在项目中有多个文件，情况如下


| 文件名           | 用途                                                                                                                    |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------- |
| main.py          | 预置选项为不冲突、未满、艺术与文学,支持 邮箱/Bark聚合推送~~停止维护~~                                                   |
| Webclass_main.py | 预置选项为不冲突、未满，支持预设课程种类，支持课程预搜索，支持激活推送模式，支持自动选课，支持校内访问(<u>推荐使用</u>) |
| bark_main.py     | 预置选项为不冲突、未满、艺术与文学，仅支持bark推送~~停止维护~~                                                          |
| Mail_main.py     | 预置选项为不冲突、未满、艺术与文学，仅支持邮箱推送~~停止维护~~                                                          |

这里以运行Webclass_main.py为例

### 6.1 Windows运行

切入项目目录,按住Shift右键，点击在终端中打开，运行`python3 Webclass_main.py`

### 6.2 Linux运行

切入项目目录运行`python3 Webclass_main.py`

# 有报错请在issue中报告
