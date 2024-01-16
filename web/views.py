import json

from django.shortcuts import render, get_object_or_404
from .models import BlogDetail, Testimonial, MenuCategory, Menu, Contact
from django.http import HttpResponse


# Create your views here.



def index(request):
  blogs = BlogDetail.objects.all()
  testimonial = Testimonial.objects.all()
  menus=Menu.objects.all()
  menucategorys = MenuCategory.objects.all()
  
  context = {
    'blogs': blogs,
    'testimonial': testimonial,
    'menus':menus,
    'menucategorys':menucategorys,
  }
  return render(request, 'web/index.html', context)


def about(request):
  return render(request, 'web/about-us.html')


def menu(request):
  menus=Menu.objects.all()
  menucategorys = MenuCategory.objects.all()
  
  context = {
    'menus':menus,
    'menucategorys':menucategorys,
  }
  return render(request, 'web/menu.html', context)


def blog(request):
  blogs = BlogDetail.objects.all()
  
  context = {
    'blogs': blogs,
  }
  return render(request, 'web/blog.html', context)

def blog_detail(request, slug):
  blog = get_object_or_404(BlogDetail, slug=slug)
  context = {'blog': blog}

  return render(request, 'web/blog_detail.html', context)



def contact(request):
    form = Contact(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }

    return render(request, 'web/contact.html', context)
