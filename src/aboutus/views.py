from django.shortcuts import render
from .models import AboutUs, Why_Choose_us, Chef

# Create your views here.
def Aboutus_list (request):
    about = AboutUs.objects.last()
    why_choose_us = Why_Choose_us.objects.all()
    chef = Chef.objects.all()

    context = {
        'about': about,
        'why_choose_us': why_choose_us,
        'chef': chef,
    }

    return render(request, 'aboutus/about.html', context)
