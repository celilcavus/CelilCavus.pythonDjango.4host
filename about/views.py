from django.shortcuts import render
from . import models
# Create your views here.
def about(request):
    result = models.AboutModel.objects.last()
    context = {
        'about':result
    }
    return render(request,'about/about.html',context)