from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Customizes the Django Admin interface for the Item model.
    Visit: http://localhost:8000/admin/items/item/
    """

    # Columns to display in the list view of items
    list_display = ['id', 'name', 'price', 'quantity', 'created_at', 'updated_at']

    # Fields the admin search bar will search in
    search_fields = ['name', 'description']

    # Filter sidebar options (right side of admin list)
    list_filter = ['created_at', 'updated_at']

    # These fields are shown but cannot be edited (auto-managed by Django)
    readonly_fields = ['created_at', 'updated_at']

    # How the form is laid out when adding/editing an item
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'quantity')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Collapsed by default
        }),
    )