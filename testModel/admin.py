from django.contrib import admin
from testModel.models import Test,Contact,Tag

class TagInline(admin.TabularInline):
        model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline

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
# 这边没再注册Tag，因为已经内联了，没必要两个地方都显示，但要显示也是可以的，如下行
admin.site.register([Test])
#admin.site.register([Test, Tag])

