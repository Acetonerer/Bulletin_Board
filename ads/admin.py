from django.contrib import admin

from .models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'author', 'created_at')
    list_filter = ('author',)
    search_fields = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'ad', 'author', 'created_at')
    list_filter = ('author',)
