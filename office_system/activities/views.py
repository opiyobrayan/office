from django.shortcuts import render
from . models import Store
# Create your views here.
def home(request):
    stores= Store.objects.all()
    return render(request,'home.html',{'stores':stores})

