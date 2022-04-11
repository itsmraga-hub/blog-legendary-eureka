from django.contrib import admin
from.models import BlogPost, Tag
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(Tag)
