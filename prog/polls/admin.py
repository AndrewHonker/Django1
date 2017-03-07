from django.contrib import admin
from polls.models import *

# Register your models here.
class GoodAdmin(admin.ModelAdmin):
	list_display=('name','category','price','description')


class CategoryAdmin(admin.ModelAdmin):
	list_display=('id','name')
admin.site.register(Good,GoodAdmin)
admin.site.register(Category,CategoryAdmin)