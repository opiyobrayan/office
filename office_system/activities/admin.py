from django.contrib import admin
from . models  import Store
from . models  import Transport
from . models  import Ticketing
from . models  import Hotel
# from . models  import Iec
from . models  import Out

# Register your models here.

# admin.site.register(Store)
admin.site.register(Transport)
admin.site.register(Hotel)
admin.site.register(Ticketing)
admin.site.register(Out)
# admin.site.register(Iec)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','amount','date','status','description')
    ordering =  ('date',)
    search_fields = ('name','amount')
    list_filter = ('amount','quantity')