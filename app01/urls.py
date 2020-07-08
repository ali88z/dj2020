from django.urls import path,re_path
from app01 import views # 从自己的 app 目录引入views 

urlpatterns = [ 
    re_path("^add_book/$", views.add_book, name='add_book'),
    re_path("^add_book2/$", views.add_book2, name='add_book2'),
]
