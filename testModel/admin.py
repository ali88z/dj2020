from django.contrib import admin
from testModel.models import Test,Contact,Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])
