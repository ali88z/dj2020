from django.http import HttpResponse
from django.shortcuts import render

def hello(req):
    # req是HttpRequest，这里面包含请求的所有信息，如body,path,
    # method等等
    # response主要3种：HttpResponse(), render(), redirect()
    return HttpResponse("Hello World!")

'''
标签：
1，过滤器
2，列表等可以用.获取成员
3，过程语法 {% if confition %}
4，标签以字典传送
'''
def runoob(req):
    #context = {}
    #context['hello'] = 'Hello World!'
    viewlist = ['list1', 'list2', 'list3']
    viewdict = {'first':'dict1', 'second':'dict2', 'third':'dict3'}
    # Django 会自动对 views.py 传到HTML文件中的标签语法进行转义，令其语义失效。
    # 加 safe 过滤器是告诉 Django 该数据是安全的，不必对其进行转义，可以让该数据语义生效
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    #return render(req, 'runoob.html', context)
    #return render(req, 'runoob.html', {'hello':'Hello'})
    return render(req, 'runoob.html', {'hello':'Hello', 'list':viewlist, 'dict':viewdict, 'vzero':[], 'view_str':views_str})


def templatetag(req):
    context = {}
    context['hello'] = 'Hello world'
    return render(req, 'templatetag.html', context)

def bootstrap(req):
    return render(req, 'bootstrap.html')

