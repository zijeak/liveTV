from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tv.models import channel,Category

class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# 把新增的 PostAdmin 也注册进来
admin.site.register(channel, ChannelAdmin)
admin.site.register(Category,CategoryAdmin)