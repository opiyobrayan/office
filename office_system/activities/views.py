from django.shortcuts import render
from .models import Store
# Create your views here.
def home(request):
    return render(request,'home.html',{})

# displaying items

def store(request):
    store_list=Store.objects.all()

    return render(request, 'store.html',{'store_list':store_list})