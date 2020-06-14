from django.contrib import admin

# Register your models here.
from .models import product,KHOBOR,orders,orderupdate

admin.site.register(product)
admin.site.register(KHOBOR)
admin.site.register(orders)
admin.site.register(orderupdate)
