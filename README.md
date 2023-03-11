# originsrv
使用 Django 构建 CDN 回源服务

## 初始化项目

创建项目并激活 venv
```bash
$ mkdir originsrv
$ cd originsrv/
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

激活后 venv 检查 python 版本
```bash
$ python -V
Python 3.10.6
```

安装 Django
```bash
$ python -m pip install Django
# 验证 Django 是否安装成功
$ python -m django --version
4.1.7
```

创建 originsrv 项目
```bash
$ django-admin startproject originsrv
```

修改 originsrv/urls.py
```python
urlpatterns = [
    path('', admin.site.urls),
]
```

试运行
```bash
$ cd originsrv
$ python manage.py runserver
Django version 4.1.7, using settings 'originsrv.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

访问上方的 URL，应该会打开 Django 管理后台

创建 webapp
```bash
$ python manage.py startapp webapp
```

初始化 Django 内置数据库表
```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

创建超级用户
```bash
python manage.py createsuperuser --username=huoyijie --email=huoyijie@huoyijie.cn
```

编辑 originsrv/settings.py
```conf
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```

## 引用
> [Django Docs](https://docs.djangoproject.com/zh-hans/4.1/)