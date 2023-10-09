from django.contrib import admin

from material.models import Material


@admin.register(Material)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'preview', 'sign_publication')
