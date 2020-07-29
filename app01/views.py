from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def add_book(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    print(book, type(book))

# 与上面的区别在于使用pk
def add_book2(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  获取出版社对象的id
    pk = pub_obj.pk
    #  给书籍的关联出版社字段 publish_id 传出版社对象的id
    book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
    print(book.__str__())
    return HttpResponse(book.__str__())

# 表与表之间的关系可分为以下三种：
# 一对多: 一个家庭有多个人，一般通过外键来实现。
# 一对一: 一个人对应一个身份证号码，也是用外健，数据字段设置 unique，也就是OneToOneField
# 多对多: 一个学生有多门课程，一个课程有很多学生，一般通过第三个表来实现关联，也就是ManyToManyField。

# 关联管理器(对象调用)
# 前提：
# 多对多（双向均有关联管理器）
# 一对多（只有多的那个类的对象有关联管理器，即反向才有）

# 语法格式：
# 正向：属性名
# 反向：小写类名加 _set
# 常用方法：
# add()：用于多对多，把指定的模型对象添加到关联对象集（关系表）中。
#       反向：小写表名_set
# create()：创建一个新的对象，并同时将它添加到关联对象集之中。
# 返回新创建的对象。

# 注意以下三者的区别
# 作者添加书
# ying.book_set.add(book)
# 作者创建并添加书
# book = wo.book_set.create(title="吸星大法", price=300, pub_date="1999-9-19", publish=pub)
# 书添加作者
# book.authors.add(chong, ying)

# 上面比较不重要，这边才重要，主要演示多对多(ManyToManyField)
def add_book3(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    book = models.Book.objects.filter(title="菜鸟教程").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    book.authors.add(chong, ying)
    return HttpResponse("Success!")

# 与上面的区别在于使用pk
def add_book4(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    #  获取作者对象的id
    pk = chong.pk
    #  获取书籍对象
    book = models.Book.objects.filter(title="冲灵剑法").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象的id
    book.authors.add(pk)
    return HttpResponse("Success!")

# 与上面的区别在于可以一次添加多个
def add_book5(request):
    book_obj = models.Book.objects.get(id=5)
    author_list = models.Author.objects.filter(id__lte=2)
    # 重复执行没有问题，表格没区别，但会有Warning, 且boot_authors表格的id会增长，并会在下一次
    # 添加有效行时体现
    #book_obj.authors.add(*author_list)  # 将 id 小于等于2的作者对象添加到这本书的作者集合中
    # 方式二：传对象 id
    book_obj.authors.add(*[1,2]) # 将 id=1 和 id=2 的作者对象添加到这本书的作者集合中
    return HttpResponse("Success!")

def add_book6(request):
    ying = models.Author.objects.filter(name="任盈盈").first()
    book = models.Book.objects.filter(title="冲灵剑法").first()
    # 反向
    ying.book_set.add(book)
    return HttpResponse("Success!")

# create()：创建一个新的对象，并同时将它添加到关联对象集之中。
# 返回新创建的对象。
def add_book7(request):
    pub = models.Publish.objects.filter(name="明教出版社").first()
    wo = models.Author.objects.filter(name="任我行").first()
    # 注意三者的区别
    book = wo.book_set.create(title="吸星大法", price=300, pub_date="1999-9-19", publish=pub)
    # book.authors.add(chong, ying)
    # ying.book_set.add(book)
    print(book, type(book))
    return HttpResponse("Success!")

def add_book8(request):
    caibook = models.Book.objects.filter(title='菜鸟教程').first()
    renauthor = models.Author.objects.filter(name='任我行').first()
    # book_set的类型也是Manager，和objects一样，两者都是继承自Manager
    # app01.Book.None <class 'django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager'>
    print(renauthor.book_set, type(renauthor.book_set))
    renauthor.book_set.add(caibook)
    res = renauthor.book_set.all()
    for i in res:
        print(i.title)

    #renauthor.book_set.remove(caibook)

    #renauthor.book_set.clear()
    return HttpResponse("Success!")

def add_book9(request):
    print('Author与au_dtail是OneToOne类型')
    print('正向')
    author = models.Author.objects.filter(name="令狐冲").first()
    res = author.au_detail.tel
    print(res, type(res))

    print('反向 AuthorDetail并没有author这个列，但因为Author与au_dtail是OneToOne关系，')
    print('所以可以这样用')
    addr = models.AuthorDetail.objects.filter(addr="黑木崖").first()
    res = addr.author.name
    print(res, type(res))

    print('ManyToManyField 正向')
    book = models.Book.objects.filter(title="菜鸟教程").first()
    res = book.authors.all()
    for i in res:
        print(i.name, i.au_detail.tel)

    print('反向 ')
    author = models.Author.objects.filter(name="任我行").first()
    res = author.book_set.all()
    for i in res:
        print(i.title)

    print('基于双下划线的跨表查询')
    print('一对多')
    print('正向：属性名称__跨表的属性名称 反向：小写类名__跨表的属性名称')
    res = models.Book.objects.filter(publish__name="明教出版社").values_list("title", "price")
    for i in res:
        print(i)

    print('反向：通过 小写类名__跨表的属性名称（book__title，book__price） 跨表获取数据。')
    res = models.Publish.objects.filter(name="明教出版社").values_list("book__title","book__price")
    for i in res:
        print(i)

    print('多对多')
    print('查询令狐冲出过的所有书籍的名字。')
    print('正向：通过 属性名称__跨表的属性名称(authors__name) 跨表获取数据：')
    res = models.Book.objects.filter(authors__name="令狐冲").values_list("title")
    for i in res:
        print(i)

    print('反向：通过 小写类名__跨表的属性名称（book__title） 跨表获取数据：')
    res = models.Author.objects.filter(name="令狐冲").values_list("book__title")
    for i in res:
        print(i)

    print('一对一')
    print('查询任我行的手机号。')
    print('正向：通过 属性名称__跨表的属性名称(au_detail__tel) 跨表获取数据。')
    res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")
    for i in res:
        print(i)

    print('反向：通过 小写类名__跨表的属性名称（author__name） 跨表获取数据。')
    res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")
    for i in res:
        print(i)
    return HttpResponse("Success!")
