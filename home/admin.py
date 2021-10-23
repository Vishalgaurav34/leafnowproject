from django.contrib import admin

from .models import Car,Contact,Corder

# Register your models here.
admin.site.register(Contact)

admin.site.register(Car)
admin.site.register(Corder)

