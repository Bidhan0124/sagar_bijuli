# shop/admin.py

from django.contrib import admin
from .models import Service, ProductCategory, Product, Electrician, ContactMessage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name', 'display_order')
    search_fields = ('name', 'description')
    list_editable = ('display_order',) # Allows editing order directly in list view

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)} # Auto-fill slug based on name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_featured', 'feature_order', 'image_preview')
    list_filter = ('is_featured', 'category')
    search_fields = ('name', 'description')
    list_editable = ('is_featured', 'feature_order', 'price') # Allow editing these in list view
    readonly_fields = ('image_preview',) # Show preview but don't make it editable here

@admin.register(Electrician)
class ElectricianAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'is_active', 'display_order', 'photo_preview')
    list_filter = ('is_active', 'specialization')
    search_fields = ('name', 'bio', 'specialization')
    list_editable = ('is_active', 'display_order', 'specialization')
    readonly_fields = ('photo_preview',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp', 'service')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'service', 'message', 'timestamp') # Make fields read-only
    list_editable = ('is_read',) # Allow marking as read

    # Optional: Add actions like 'Mark as read' / 'Mark as unread'
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"

    actions = [mark_as_read, mark_as_unread]

