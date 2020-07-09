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
    return HttpResponse("Success!")

def add_book9(request):
    return HttpResponse("Success!")
