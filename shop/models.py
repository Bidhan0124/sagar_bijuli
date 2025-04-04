# shop/models.py

from django.db import models
from django.utils import timezone
from django.utils.html import format_html # For image previews in admin
from phonenumber_field.modelfields import PhoneNumberField


# --- Service Model ---
class Service(models.Model):
    """Model to store information about services offered."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(help_text="Brief description of the service.")
    # Store the name of a Lucide icon (e.g., 'wrench', 'settings-2', 'tool')
    # See https://lucide.dev/ for icon names
    icon_name = models.CharField(max_length=50, blank=True, help_text="Lucide icon name (e.g., 'wrench'). Optional.")
    # Add an order field if you want to control the display sequence
    display_order = models.PositiveIntegerField(default=0, help_text="Order in which services appear (lower numbers first).")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['display_order', 'name'] # Order by custom order, then name


# --- Product Model ---
class ProductCategory(models.Model):
    """Optional: Category for products."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=110, unique=True, help_text="URL-friendly version of the name (auto-generated if left blank).")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Product Categories"

    # Optional: Auto-generate slug if needed (uncomment save method)
    # from django.utils.text import slugify
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)


class Product(models.Model):
    """Model to store information about products sold."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Optional: Link to a category
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Price in NPR. Leave blank if not applicable.")
    # Requires Pillow: pip install Pillow
    image = models.ImageField(upload_to='products/', null=True, blank=True, help_text="Upload a product image.")
    is_featured = models.BooleanField(default=False, help_text="Feature this product on the homepage?")
    # Add an order field for featured products
    feature_order = models.PositiveIntegerField(default=0, help_text="Order for featured products (lower numbers first).")


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-is_featured', 'feature_order', 'name'] # Featured first, then by order, then name

    # Optional: Method for admin preview
    def image_preview(self):
        if self.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', self.image.url)
        return "(No image)"
    image_preview.short_description = 'Image Preview'


# --- Electrician Model ---
class Electrician(models.Model):
    """Model to store information about electricians."""
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='electricians/', null=True, blank=True, help_text="Upload a photo of the electrician.")
    bio = models.TextField(blank=True, help_text="Short biography or description.")
    specialization = models.CharField(max_length=100, blank=True, help_text="e.g., Residential Wiring, Industrial Maintenance")
    display_order = models.PositiveIntegerField(default=0, help_text="Order in which electricians appear (lower numbers first).")
    contact = PhoneNumberField(null=True, blank=True, help_text='Phone number')
    is_active = models.BooleanField(default=True, help_text="Show this electrician on the site?")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['display_order', 'name']

    # Optional: Method for admin preview
    def photo_preview(self):
        if self.photo:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px; border-radius: 50%;" />', self.photo.url)
        return "(No photo)"
    photo_preview.short_description = 'Photo Preview'


# --- Contact Message Model (from previous version) ---
class ContactMessage(models.Model):
    """Model to store messages submitted through the contact form."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} ({self.email}) on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

