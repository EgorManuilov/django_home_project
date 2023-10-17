from django.contrib import admin
from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title_post', 'content_post', 'image_post', 'publ_on_off')