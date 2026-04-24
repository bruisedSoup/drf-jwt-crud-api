from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Customizes the Django Admin interface for the Item model.
    Visit: http://localhost:8000/admin/items/item/
    """

    list_display = ['id', 'name', 'price', 'quantity', 'created_at', 'updated_at']

    search_fields = ['name', 'description']

    list_filter = ['created_at', 'updated_at']

    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'quantity')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  
        }),
    )