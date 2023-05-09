from django.forms import ModelForm, widgets
from checkout.models import ContactInfo


class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        exclude = ["id"]
        fields = [
            "full_name",
            "phone_number",
            "street_name",
            "house_number",
            "city",
            "postal_code",
        ]

        widgets = {
            "full_name": widgets.TextInput(attrs={
                'class': 'form-control mb-3 contact-info-form',
                'placeholder': 'Enter your full name...'
            }),
            "phone_number": widgets.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Enter your phone number...'
            }),
            "street_name": widgets.TextInput(attrs={
                'class': 'form-control mb-3 contact-info-form',
                'placeholder': 'Enter your street name...'
            }),
            "house_number": widgets.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Enter your street number...'
            }),
            "city": widgets.TextInput(attrs={
                'class': 'form-control mb-3 contact-info-form',
                'placeholder': 'Enter your city...'
            }),
            "postal_code": widgets.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Enter your postal code...'
            })
        }
