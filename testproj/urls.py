"""testproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path
from django.conf.urls import url,include
from . import views,testdb,search

urlpatterns = [
    # path('xxx/')应该类似于re_path(r'^xxx/'), 没确认
    path('admin/', admin.site.urls),
    #url(r'^$', views.hello),
    # zjwcheck, name can use reverse(name) to route to real url
    re_path(r'^$', views.hello, name='default'),
    re_path(r'^runoob/$', views.runoob),

    re_path(r'^templatetag/$', views.templatetag),
    re_path(r'^bootstrap/$', views.bootstrap, name='aaa'),
    re_path(r'^testdb/$', testdb.testdb, name='testdb'),

    re_path(r'^search_get/$', search.search_get),
    re_path(r'^search/$', search.search),
    #url(r'^search_post/$', search.search_post),
    re_path(r'^search_post/$', search.search_post),

    # 有名分组与无名分组不能混用
    re_path("^index2/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.index)    ,
    re_path("^index/([0-9]{4})/([0-9]{2})/$", views.index),

    re_path("^testurlinclude/", include("testurlinclude.urls")),
    # zjw check reverse在模板和views里都可以用
    re_path("^route_reverse/$", views.route_reverse, name='r_reverse'),
    # zjw check reverse 无名分组在模板和views里都可以用
    re_path("^route_reverse2/([0-9]{2})/$", views.route_reverse2, name='r_reverse2'),
]
