from django.contrib import admin
from .models import Country, City, Sex, ExtendedUser
# Register your models here.


admin.site.register(Country)
admin.site.register(City)
admin.site.register(Sex)
admin.site.register(ExtendedUser)
