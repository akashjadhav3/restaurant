from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
from aboutus.models import Why_Choose_us

# Create your views here.
def home_page(request):
    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    post = Post.objects.all()
    why_choose_us = Why_Choose_us.objects.all()
    latest_post = Post.objects.last()

    context = {
        'meals':meals,
        'meal_list': meal_list,
        'categories': categories,
        'posts': post,
        'latest_post': latest_post,
        'why_choose_us': why_choose_us,

    }
    return render (request, 'home/index.html', context )
