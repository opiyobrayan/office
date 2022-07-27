from django.db import models


# Create your models here.

class Store(models.Model):
    name = models.CharField('Product Name', max_length=120)
    quantity = models.IntegerField('quantity', max_length=120, blank=True,null=True)
    amount = models.IntegerField('Amount', max_length=120)
    status = models.CharField( 'status', max_length=120)
    date= models.DateTimeField('Date')
    description= models.TextField('description', blank=True,null=True)

    def __str__(self):
        return self.name

class Transport(models.Model):
    name = models.CharField('Name of Company', max_length=120)
    contact = models.IntegerField('Contact Person', max_length=120)
    mobile = models.IntegerField('Telephone number', max_length=120)
    email= models.EmailField('Email Address')
    services = models.CharField('services', max_length=120)
    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField('Name of Hotel', max_length=120)
    accommadate= models.CharField('accommadate', max_length=120)
    confernce = models.CharField('conference', max_length=120)
    contact_name = models.CharField('contact name', max_length=120)
    contact_mobile =  models.CharField('contact mobile', max_length=120)
    email= models.EmailField('Email Address')

    def __str__(self):
        return self.name

class Ticketing(models.Model):
    name = models.CharField('Name of Company', max_length=120)
    contact = models.IntegerField('Contact Person', max_length=120)
    mobile = models.IntegerField('Telephone number', max_length=120)
    email= models.EmailField('Email Address')
    services = models.CharField('services', max_length=120)
    def __str__(self):
        return self.name

