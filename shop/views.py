# shop/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import ContactForm
from .models import Service, Product, Electrician # Import new models
import json

def index(request):
    """
    View function to render the main shop page (index.html).
    Fetches services, featured products, and active electricians to display.
    """
    # Fetch data from the database
    services = Service.objects.all() # Get all services, ordered by display_order (defined in model Meta)
    featured_products = Product.objects.filter(is_featured=True) # Get only featured products, ordered by feature_order
    electricians = Electrician.objects.filter(is_active=True) # Get only active electricians

    # Pass data to the template context
    context = {
        'page_title': "Sagar Bijuli Pasal - Tokha",
        'services': services,
        'products': featured_products, # Pass featured products specifically
        'electricians': electricians,
    }
    return render(request, 'shop/index.html', context)


@require_POST
def contact_submit(request):
    """
    View function to handle the contact form submission via AJAX (POST).
    Validates the form data and saves it if valid.
    Returns a JSON response indicating success or failure.
    (No changes needed from previous version for this view)
    """
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    try:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optional: Send email notification here
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
        else:
            errors = {field: error[0] for field, error in form.errors.items()}
            return JsonResponse({'status': 'error', 'message': 'Please correct the errors below.', 'errors': errors}, status=400)
    except Exception as e:
        print(f"Error processing contact form: {e}") # Replace with proper logging
        return JsonResponse({'status': 'error', 'message': 'An unexpected error occurred. Please try again later.'}, status=500)

