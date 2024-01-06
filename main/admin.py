from django.contrib import admin

from .models import *

class FormAdmin(admin.ModelAdmin):
    list_display = ['name','email']

admin.site.register(Choose)
admin.site.register(Choose_enjoy)
admin.site.register(gallery)
admin.site.register(Order)
