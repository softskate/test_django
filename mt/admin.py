from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url', 'named_url', 'menu_name', 'order')
    list_editable = ('parent', 'url', 'named_url', 'menu_name', 'order')

admin.site.register(MenuItem, MenuItemAdmin)