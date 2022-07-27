
from django.urls import path

from office_system.activities import views

urlpatterns = [

    path('',views.home, name='home')
]
