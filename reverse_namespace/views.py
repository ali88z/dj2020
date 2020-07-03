from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, 'reverse_namespace.html')
    # 下面这个会变死循环，但是可以演示reverse namespace
    #return redirect(reverse('reverse_namespace:index'))
