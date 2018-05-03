from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","auther","content","create_time","last_updated_time","is_deleted","readed_num" )
    ordering = ("-id",) # - 表示倒序
admin.site.register(Article,ArticleAdmin)