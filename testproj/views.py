from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse

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

def index(req, year, month):
    s = "index test "+year+" "+month
    return HttpResponse(s)

def route_reverse(req):
    ctx = {}
    if 'q' in req.POST and req.POST['q'] == 'redirect':
        #return redirect("/")
        return redirect(reverse('default'))
    elif 'q' in req.POST and req.POST['q'] == '10':
        # reverse 无名分组
        return redirect(reverse('r_reverse2', args=(req.POST['q'],)))
    elif 'q' in req.POST and req.POST['q'] == '2020':
        # reverse 有名分组
        return redirect(reverse('r_reverse3', kwargs={'year':req.POST['q']}))
    else:
        ctx['rlt'] = "input redirect or 10 or 2020 to test"
        return render(req, 'route_reverse.html', ctx)

def route_reverse2(req, month):
    str = 'route_reverse2 ' + month
    return HttpResponse(str)

def route_reverse3(req, year):
    str = 'route_reverse3 ' + year
    return HttpResponse(str)
