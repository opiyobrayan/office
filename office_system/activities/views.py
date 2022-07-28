import csv

from django.shortcuts import render
from .models import Store
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{})

# displaying items

def store(request):
    store_list=Store.objects.all()

    return render(request, 'store.html',{'store_list':store_list})

# report view
def report_view(request):
    return render(request,'report_view.html',{})

# add csv and saving

def store_csv(request):

    response= HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=stores.csv'

    writer=csv.writer(response)

    stores=Store.objects.all()

    writer.writerow(['product name','quantity','last modified','action'])
    list1=[]
    for s in stores:
        writer.writerow([s.name,s.quantity,s.date,s.status])


    return response



