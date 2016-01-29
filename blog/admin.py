from blog.models import Tag, Author, Article
from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)

class ArticleAdmin(MarkdownModelAdmin):
    list_display = ('caption',  'author', 'publish_time', 'update_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)




admin.site.register(Article, ArticleAdmin)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)

