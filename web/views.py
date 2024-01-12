from django.shortcuts import render
from .models import BlogDetail

# Create your views here.



def index(request):
  blogs = BlogDetail.objects.all()
  
  context = {
    'blogs': blogs,
  }
  return render(request, 'web/index.html', context)

