# Project Plan Management Platform

## 0.配置该项目的 python 虚拟环境

创建一个python虚拟环境create a virtual environment

    python -m venv <venv_name>

激活虚拟环境activate the virtual environment:

    .\venv_name\Scripts\activate

为虚拟环境安装python项目的依赖

    pip install -r requirements.txt

关闭虚拟环境deactivate the virtual environment:

    deactivate

配置 vscode python 代码解析器

- ctrl+shift+p

![Alt text](doc/docimg/image.png)

- python 选择解释器
![Alt text](doc/docimg/image1.png)

- 选择输入路径
![Alt text](doc/docimg/image-1.png)

- 选择 <venv_name>/Script/python.exe, 完成

![Alt text](doc/docimg/image-2.png)

新建 terminal 时 终端 自动启动虚拟环境, 输入行前方出现 (<venv_name>) 则为配置成功，该项目终端自动激活对应虚拟环境

    PS F:\dictionary\Campus\Fall2023\CSE 389\Codes\project> & c:/Users/ZK/Desktop/Projects/omen_venv/Scripts/Activate.ps1

    (<venv_name>) PS F:\dictionary\Campus\Fall2023\CSE 389\Codes\project> 



## 1.日常使用配置好的 python 虚拟环境

激活虚拟环境activate the virtual environment:

    .\venv_name\Scripts\activate

关闭虚拟环境deactivate the virtual environment:

    deactivate

添加包

    pip install <package_name>

生成/更新 生成的python虚拟环境

    pip freeze > requirement.txt

## 2.测试开发 django 项目

启动开发服务器 Start Server

    python manage.py runserver 

创建新应用 Create app

    python manage.py startapp <appname>

创建新用户

    python manage.py createsuperuser <username>

数据迁移 migrate

    python manage.py makemigrations <appname>

    python manage.py migrate

建议网站admin 账号密码 Admin

    username: admin
    password: admin
