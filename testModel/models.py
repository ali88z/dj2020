from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name
 
class Tag(models.Model):
    # CASCADE：此值设置，是级联删除。
    # PROTECT：此值设置，是会报完整性错误。
    # SET_NULL：此值设置，会把外键设置为 null，前提是允许为 null。
    # SET_DEFAULT：此值设置，会把设置为外键的默认值。
    # SET()：此值设置，会调用外面的值，可以是一个函数。一般情况下使用 CASCADE 就可以了。
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    title = models.CharField(max_length=32) # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2) # 书籍价格
    publish = models.CharField(max_length=32) # 出版社名称
    pub_date = models.DateField() # 出版时间
