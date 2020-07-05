from django.contrib import admin
from testModel.models import Test,Contact,Tag

class ContactAdmin(admin.ModelAdmin):
    # fields 属性定义了要显示的字段。zjw check, 这样是只显示这边有的，但是在添加数据时
    # 也是一样只显示这边列的，要是没显示的项没有默认值将导致Add出错
    # fields = ('name', 'email')

    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            # zjw check, 这里的classes是怎么工作的不知道
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
 
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])

