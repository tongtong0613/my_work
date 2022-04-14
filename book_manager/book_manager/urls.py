"""book_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('', include('book.urls')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=r'media/favicon.ico')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATICFILES_DIRS}), # 收集静态文件时关闭
    # path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), # 收集静态文件时打开，然后关闭STATICFILES_DIRS
]
