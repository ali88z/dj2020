from django.urls import path,re_path
from testurlinclude import views # 从自己的 app 目录引入views 

urlpatterns = [ 
    re_path("^index/$", views.index), 
]
