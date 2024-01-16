from django.contrib import admin
from .models import BlogDetail, Testimonial, Menu, MenuCategory, Contact
# Register your models here.


@admin.register(BlogDetail)
class BlogDetailAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "content")


@admin.register(Menu)
class menuAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "price")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

