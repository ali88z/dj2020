from django.http import HttpResponse

from testModel.models import Test

gindex=0
def testdb(req):
    global gindex
    gindex += 1
    res = ""
    t = Test.objects.all()
    if t and len(t) > 3:
        t[0].delete()  # t[0:2} is ok
    t = Test(name=str(gindex))
    t.save()
    # zjw error here, 结合下面，update应该只有在查询的结果中才能用
    #t.update(name='haha')

    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    # 修改所有的列
    # Test.objects.all().update(name='Google')

    list = Test.objects.all()
    for x in list:
        res += x.name+" "
    return HttpResponse("<p>" + res + "</p>")
