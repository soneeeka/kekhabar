from django.shortcuts import render
from .models import PostModel,CategoryModel
# Create your views here.
import datetime
def news(request):
    # sports_category=CategoryModel.objects.filter(name='Sports').first()
    # # for category in categories:
    # #     sports_category=category
    # posts=PostModel.objects.filter(category=sports_category)
    posts=PostModel.objects.filter(posted_on__gte=datetime.date(2020,3,20))
    # posts=PostModel.objects.filter(title__startswith ='R')
    # sports_category=CategoryModel.objects.filter(name='Sports').first()
    # posts=PostModel.objects.exclude(title__startswith ='R').filter(category=sports_category)

    context={
    'posts':posts
        }
    return render(request,'newsapp/news.html',context)
def details(request,id):
    posts=PostModel.objects.filter(id=id).first()
    context={
        'posts':posts
    }
    return render(request,'newsapp/details.html',context)

