# shop/urls.py

from django.urls import path
from . import views # Import views from the current directory

app_name = 'shop' # Optional: namespace for URLs

urlpatterns = [
    # Map the root URL of the app ('/') to the index view
    path('', views.index, name='index'),
    # Map the '/contact-submit/' URL to the contact_submit view for handling form POST requests
    path('contact-submit/', views.contact_submit, name='contact_submit'),
]
