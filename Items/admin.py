from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'original_price', 'sale_price']

admin.site.register(Item, ItemAdmin)