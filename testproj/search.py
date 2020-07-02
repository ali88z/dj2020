from django.http import HttpResponse
from django.shortcuts import render,redirect

def search_get(req):
    return render(req, 'search_get.html')

def search(req):
    req.encoding = 'utf-8'
    if 'q' in req.GET and req.GET['q']:
        message = 'Search: ' + req.GET['q']
    else:
        message = 'Search empty!'

    return HttpResponse(message)

def search_post(req):
    ctx = {}
    req.encoding = 'utf-8'
    # 可用于调试，类似下面的内容 check
    # b'csrfmiddlewaretoken=IAMVjQmgv1LwO87ZDlSVxLfgMDJeiCPT0Cr7sm0b8gZekKBIsAOZChzBTp6ITzdW&q=fff'
    #print(req.body)
    #print(req.path)
    if 'q' in req.POST and req.POST['q']:
        ctx['rlt'] = req.POST['q']

    return render(req, 'search_post.html', ctx)
    # check
    #return redirect("/")
