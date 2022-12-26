from django.contrib import admin

# Register your models here.
from  . models import Catagory,Products

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Catagory,CatagoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','availiable','created','updated']
    list_editable = ['price','stock','availiable']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Products,ProductAdmin)