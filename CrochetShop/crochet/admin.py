from django.contrib import admin
from .models import Crochet

class CrochetAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')



admin.site.register(Crochet, CrochetAdmin)