from django.http import HttpResponse

from testModel.models import Test,Contact,Tag,Book

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

def modelbook(req):
    #book = Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8") 
    #book.save()

    # 与上面类似，但更简洁，推荐
    #books = Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10") 
    #print(books, type(books)) # Book object (18) 

    print('# 下面这些都有类似上面的直接使用模型类操作的方式，但用objects更简洁')
    # 返回值：元组，第一个元素为受影响的行数。
    # books=Book.objects.filter(pk__in=[1,2]).delete()
    # books=models.Book.objects.delete()　 # 报错
    # books=models.Book.objects.all().delete()　　 # 删除成功

    # QuerySet 类型数据.update(字段名=更改的数据)（推荐）
    # 返回值：整数，受影响的行数
    #books = Book.objects.filter(pk__in=[7,8]).update(price=888)

    print("//////////////////////////////////////")
    books = Book.objects.all() 
    print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。

    print("//////////////////////////////////////")
    books = Book.objects.filter(pk=5) # pk应该是primarykey
    print(books)
    books = Book.objects.filter(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。

    print("//////////////////////////////////////")
    books = Book.objects.exclude(pk=5)
    print(books)
    books = Book.objects.exclude(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。

    print('# get() 方法用于查询符合条件的返回模型类的对象符合条件的对象只能为一个，如果符合筛选条件的对象超过了一个或者没有一个都会抛出错误，注意这个返回是Book类型')
    books = Book.objects.get(pk=5)
    #books = Book.objects.get(pk=18)  # 报错，没有符合条件的对象
    #books = Book.objects.get(price=200)  # 报错，符合条件的对象超过一个
    print(books, type(books))  # 模型类的对象

    print("# 注意逆序可以用-或reverse，这边的逆序跟可能跟想像不太一样，建议查手册，从结果上看应该所有操作都是以数据库的操作为准")
    # 价钱 5:200 1:300 2/3/4:302
    books = Book.objects.order_by("price") # 查询所有，按照价格升序排列 # 5 1 2 3 4
    print(books, type(books))  # QuerySet类型
    books = Book.objects.order_by("-price") # 查询所有，按照价格降序排列 # 2 3 4 1 5
    print(books, type(books))  # QuerySet类型
    books = Book.objects.order_by("-price").reverse() # 5 1 2 3 4
    print(books, type(books))  # QuerySet类型

    books = Book.objects.count() # 查询所有数据的数量 
    print(books, type(books))
    books = Book.objects.filter(price=200).count() # 查询符合条件数据的数量
    print(books, type(books))

    books = Book.objects.first() # 返回所有数据的第一条数据
    print(books, type(books))
    books = Book.objects.last() # 返回所有数据的最后一条数据
    print(books, type(books))

    books = Book.objects.all().exists()
    print(books, type(books))
    # 报错，判断的数据类型只能为 QuerySet 类型数据，不能为整型和模型类的对象。
    # books = Book.objects.exists()
    books = Book.objects
    # objects的类型是django.db.models.manager.Manager
    print(books, type(books))
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为整型
    # books = Book.objects.count().exists()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为模型类对象
    # books = Book.objects.first().exists()

    print('# values() 方法用于查询部分字段的数据。返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个可迭代的字典序列，字典里的键是字段，值是数据。')
    print('查询所有的id字段和price字段的数据')
    books = Book.objects.values("pk","price")
    print(books, type(books))
    print(books[0]["price"],type(books)) # 得到的是第一条记录的price字段的数据

    print('# values_list() 方法用于查询部分字段的数据。返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个个元组，元组里放的是查询字段对应的数据。')
    # 查询所有的price字段和publish字段的数据
    books = Book.objects.values_list("price","publish")
    print(books, type(books))
    print(books[0][0],type(books)) # 得到的是第一条记录的price字段的数据

    print('# distinct() 方法用于对数据进行去重。 返回的是 QuerySet 类型数据。 注意：对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。distinct() 一般是联合 values 或者 values_list 使用。')
    print('查询一共有多少个出版社')
    books = Book.objects.values_list("publish").distinct() # 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
    print(books, type(books))
    books = Book.objects.distinct()
    print(books, type(books))

    print('# filter() 方法基于双下划线的模糊查询（exclude 同理）。注意：filter 中运算符号只能使用等于号 = ，不能使用大于号 > ，小于号 < ，等等其他符号。__in 用于读取区间，= 号后面为列表 。')
    print('注意上面这句话说的exclude，也就是说下面这些基本都可以用于exclude')
    print('查询价格为200或者300的数据, 注意这个是200或300，不是200~300之间，与下面的price__range区别开')
    books = Book.objects.filter(price__in=[200,300])
    print(books, type(books))
    books = Book.objects.exclude(price__in=[200,300])
    print(books, type(books))
    print('查询价格大于200的数据 ')
    books = Book.objects.filter(price__gt=200)
    print(books, type(books))
    print('查询价格大于等于200的数据 ')
    books = Book.objects.filter(price__gte=200)
    print(books, type(books))
    print('查询价格小于300的数据 ')
    books=Book.objects.filter(price__lt=300)
    print(books, type(books))
    print('查询价格小于等于300的数据 ')
    books=Book.objects.filter(price__lte=300)
    print(books, type(books))
    print('__range 在 ... 之间，左闭右闭区间，= 号后面为两个元素的列表。')
    print('查询价格为200到300之间的数据，注意这个是200~300之间，不是200或300，与上面的price__in区别开')
    books=Book.objects.filter(price__range=[200,300])
    print(books, type(books))
    print('__contains 包含，= 号后面为字符串。')
    books=Book.objects.filter(title__contains="菜")
    print(books, type(books))
    print('__icontains 不区分大小写的包含，= 号后面为字符串。')
    books=Book.objects.filter(title__icontains="python")
    print(books, type(books))
    print('__startswith 以指定字符开头，= 号后面为字符串。')
    books=Book.objects.filter(title__startswith="菜")
    print(books, type(books))
    print('__endswith 以指定字符结尾，= 号后面为字符串。')
    books=Book.objects.filter(title__endswith="教程")
    print(books, type(books))
    print('__year 是 DateField 数据类型的年份，= 号后面为数字。')
    books=Book.objects.filter(pub_date__year=2008) 
    print(books, type(books))
    print('__month 是DateField 数据类型的月份，= 号后面为数字。')
    books=Book.objects.filter(pub_date__month=10)
    print(books, type(books))
    print('__day 是DateField 数据类型的天数，= 号后面为数字。')
    books=Book.objects.filter(pub_date__day=1)
    print(books, type(books))

    return HttpResponse("<p>数据添加成功！</p>")
