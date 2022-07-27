from django.contrib import admin
from . models  import Store
from . models  import Transport
from . models  import Ticketing
from . models  import Hotel

# Register your models here.

# admin.site.register(Store)
admin.site.register(Transport)
admin.site.register(Hotel)
admin.site.register(Ticketing)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','amount','date','status','description')
    ordering =  ('date',)
    search_fields = ('name','amount')
    list_filter = ('amount','quantity')