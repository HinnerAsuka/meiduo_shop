"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# 总路由中注册自定义转换器
from utils.converters import UsernameConverter, MobileConverter
from django.urls import register_converter

register_converter(UsernameConverter, 'Username')
register_converter(MobileConverter, 'Mobile')

urlpatterns = [
    path('admin_manage/', admin.site.urls),
    # 导入users子应用的路由
    path('', include('apps.users.urls')),
    path('', include('apps.verify.urls')),
    path('', include('apps.oauth.urls')),
    path('', include('apps.areas.urls')),
    path('', include('apps.goods.urls')),
    path('', include('apps.carts.urls')),
    path('', include('apps.orders.urls')),
    path('', include('apps.pay.urls')),
    path('meiduo_admin/', include('apps.admin_manage.urls')),
]
