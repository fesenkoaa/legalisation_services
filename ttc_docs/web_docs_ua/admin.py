from django.contrib import admin
from .models import *


class UaCategoryAdmin(admin.ModelAdmin):

    list_display = ('category', )
    list_display_links = ('category', )
    list_filter = ['chapter', ]


class UaArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'category', 'title', 'date')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('category',)


class UaAdviseAdmin(admin.ModelAdmin):

    list_display = ('id', 'preview', 'text')
    list_display_links = ('preview',)
    search_fields = ('preview',)


admin.site.register(CategoryUa, UaCategoryAdmin)
admin.site.register(ArticleUa, UaArticleAdmin)
admin.site.register(AdvisesUa, UaAdviseAdmin)