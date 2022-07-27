from activities.models import  Store
# from . models  import Store


def data_csv():
    stores= Store.objects.all()
    print(stores)