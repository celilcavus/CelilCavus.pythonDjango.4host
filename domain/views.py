from django.shortcuts import render

# Create your views here.
def domain(request):
    return render(request,'domain/domain.html')