from django.urls import path
from .import views

app_name = 'web'
urlpatterns = [
    path('',views.index,name='index'),
    path('about-us',views.about,name='about'),
    path('menu',views.menu,name='menu'),
    path('blog',views.blog,name='blog'),
    path('blog/<slug>/',views.blog_detail,name='blog_detail'),
    path('contact',views.contact,name='contact'),
]
