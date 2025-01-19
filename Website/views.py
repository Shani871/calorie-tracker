from django.shortcuts import render

from Website.models import Food


# Create your views here.
def index(request):
    foods = Food.objects.all()
    return render(request,'index.html',{'foods':foods})
