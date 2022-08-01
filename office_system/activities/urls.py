
from django.urls import path

from . import views

urlpatterns = [

    path('',views.home, name='home'),
    path('store', views.store, name='store'),
    # path('report-view', views.report_view, name='report-view'),
    path('store-csv', views.store_csv, name='store-csv'),



]
