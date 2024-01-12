from django.contrib import admin
from .models import BlogDetail
# Register your models here.


@admin.register(BlogDetail)
class BlogDetailAdmin(admin.ModelAdmin):
    list_display = ("name", "date")

