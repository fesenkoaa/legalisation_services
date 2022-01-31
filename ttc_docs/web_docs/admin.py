from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('category', )
    list_display_links = ('category', )
    list_filter = ['chapter', ]


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'category', 'title', 'date')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('category',)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'auth', 'message', 'date')
    list_display_links = ('auth',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone', 'date')
    list_display_links = ('id',)


class AdviseAdmin(admin.ModelAdmin):

    list_display = ('id', 'preview', 'text')
    list_display_links = ('preview',)
    search_fields = ('preview',)


class AppImageAdmin(admin.ModelAdmin):

    list_display = ('id', 'title')


class ServicesCategoryAdmin(admin.ModelAdmin):

    list_display = ('category',)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('category', 'service_name', 'service_name_ua')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Advises, AdviseAdmin)
admin.site.register(AppImage, AppImageAdmin)
admin.site.register(ServiceCategory, ServicesCategoryAdmin)
admin.site.register(Services, ServicesAdmin)