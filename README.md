mysite
====
项目简介：
-------
mysite是基于python3.6+Django 1.11.6+Bootstrap3开发的个人博客项目，支持用户登录、注册、修改密码、个人信息展示页等功能；博客的增删改查、评论、点赞、分类展示等功能；图片的上传、分类展示和删除功能；学习课程的增删改查功能

使用方法：
-------
1.安装Python3.6环境
-------
2.下载代码到本地并解压
-------
3.cmd到根目录下安装相关依赖包
-------
```
pip install -r requirements.txt
```
4.安装mysql数据库，进入mysite/settings.py配置数据库连接
-------

```DATABASES = {
‘default’: {
    # 'ENGINE': 'django.db.backends.sqlite3',
    # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    'ENGINE':'django.db.backends.mysql',     # 数据库类型，mysql
    'NAME':'mysite',            #  database名
    'USER':'root',               # 登录用户
    'PASSWORD':'123456',        #  登录用户名
    'HOST':'127.0.0.1',        # 数据库地址
    'PORT':'3306'              # 数据库端口
}
}
```
5.cmd到根目录下，生成数据库迁移记录
-------
```
python manage.py makemigrations
```
6.完成数据库迁移
-------
```
python manage.py migrate 
```
7.创建超级用户，用于后台管理
-------
```
python manage.py createsuperuser
```
8.运行启动django服务
-------
```
python manage.py runserver 127.0.0.0:8000
```
9.访问127.0.0.0:8000/login进入登录页面
-------
![](https://github.com/PyGuojun/mysite_login/blob/master/image/login.png)

