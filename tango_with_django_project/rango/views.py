from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page


def index(request):
    #used to retrieve the top 5 categories
    category_list = Category.objects.order_by('-likes')[:5]
    top_pages = Page.objects.order_by('-views')[:5]  # Fetch top five most viewed pages

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    try:
        context_dict['pages'] = top_pages
    except Category.DoesNotExist:
        context_dict['pages'] = None

    return render(request, 'rango/index.html', context=context_dict)

def about(response):
    context_dict = {'boldmessage': 'This tutorial has been put together by Andrew'}
    return render(response,'rango/about.html',context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category
        
    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request,'rango/category.html', context=context_dict)