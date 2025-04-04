# shop/forms.py

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """
    Django Form based on the ContactMessage model for validation.
    """
    class Meta:
        model = ContactMessage
        # Fields to include in the form (match the HTML form 'name' attributes)
        fields = ['name', 'email', 'service', 'message']
        # Optional: Customize widgets if needed (e.g., for styling or attributes)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'John Doe', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-primary focus:border-primary transition duration-300'}),
            'email': forms.EmailInput(attrs={'placeholder': 'john.doe@example.com', 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-primary focus:border-primary transition duration-300'}),
            'service': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-primary focus:border-primary transition duration-300 bg-white'}),
            'message': forms.Textarea(attrs={'placeholder': 'How can we help you today?', 'rows': 4, 'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-primary focus:border-primary transition duration-300'}),
        }
        # Optional: Customize labels if they differ from model field names
        # labels = {
        #     'name': 'Your Full Name',
        # }
        # Optional: Customize help texts
        # help_texts = {
        #     'email': 'We will never share your email.',
        # }

    # Add the service choices directly to the form field
    # Ensure these match the <option value="..."> in your HTML exactly
    SERVICE_CHOICES = [
        ('', '-- Select a Service --'), # Empty value for placeholder
        ('fitting', 'Fitting / Installation'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
        ('product_query', 'Product Query'),
        ('other', 'Other'),
    ]
    service = forms.ChoiceField(choices=SERVICE_CHOICES, required=False, widget=forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-primary focus:border-primary transition duration-300 bg-white'}))

