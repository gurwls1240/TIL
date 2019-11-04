from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at',)
    list_display_links = ('content',)
    list_filter = ('created_at',)
    list_editable = ('title',)
    list_per_page = 2

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk','content','created_at','updated_at',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)