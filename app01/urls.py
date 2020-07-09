from django.urls import path,re_path
from app01 import views # 从自己的 app 目录引入views 

urlpatterns = [ 
    re_path("^add_book/$", views.add_book, name='add_book'),
    re_path("^add_book2/$", views.add_book2, name='add_book2'),
    re_path("^add_book3/$", views.add_book3, name='add_book3'),
    re_path("^add_book4/$", views.add_book4, name='add_book4'),
    re_path("^add_book5/$", views.add_book5, name='add_book5'),
    re_path("^add_book6/$", views.add_book6, name='add_book6'),
    re_path("^add_book7/$", views.add_book7, name='add_book7'),
    re_path("^add_book8/$", views.add_book8, name='add_book8'),
    re_path("^add_book9/$", views.add_book9, name='add_book9'),
]
