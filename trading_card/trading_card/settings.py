"""
Django settings for trading_card project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$+qhk0$xmyar4z()*cuywy@q!8h-1*%5d3r6jl3b*j9x9n)q+j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'card',
    'xadmin',
    'crispy_forms',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trading_card.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'trading_card.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
ip = '127.0.0.1'
DATABASE_NAME = 'trading_card'  # mysql数据库名称
DATABASE_USER = 'root'  # mysql数据库用户名
DATABASE_PASS = '1q2w3e4r'  # mysql数据库密码
DATABASE_HOST = ip  # mysql数据库IP
DATABASE_PORT = 3306  # mysql数据库端口

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASS,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
        'OPTIONS': {'charset': 'utf8mb4', },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 使用中国时区

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # 收集静态文件时打开，然后关闭STATICFILES_DIRS

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_USER_ICON = os.path.join(BASE_DIR, 'media/user_icon')

IMPORT_EXPORT_USE_TRANSACTIONS = True
# 在导入数据时使用数据库事务，默认False

SIMPLEUI_HOME_INFO = False

SIMPLEUI_CONFIG = {
    # 是否使用系统默认菜单，自定义菜单时建议关闭。
    'system_keep': False,

    # 用于菜单排序和过滤, 不填此字段为默认排序和全部显示。空列表[] 为全部不显示.
    'menu_display': ['卡片Checklist', '权限认证'],

    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时刷新展示菜单内容。
    # 一般建议关闭。
    'dynamic': False,
    'menus': [
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户列表',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-th-list',
                    'url': 'auth/group/'
                }
            ]
        },

        {
            'name': '卡片Checklist',
            'icon': 'fab fa-blogger',
            'models': [
                {
                    'name': '2022-2023赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2022_2023/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2021-2022赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2021_2022/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2020-2021赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2020_2021/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2019-2020赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2019_2020/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2018-2019赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2018_2019/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2017-2018赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2017_2018/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2016-2017赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2016_2017/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2015-2016赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2015_2016/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2014-2015赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2014_2015/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2013-2014赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2013_2014/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2012-2013赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2012_2013/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2011-2012赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2011_2012/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2010-2011赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2010_2011/',
                    'icon': 'fas fa-book'
                },
                {
                    'name': '2009-2010赛季',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。
                    'url': '/admin/card/card_2009_2010/',
                    'icon': 'fas fa-book'
                },
            ]
        },
    ]
}