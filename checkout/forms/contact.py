from django.forms import ModelForm, widgets, ValidationError
from checkout.models import ContactInfo


class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        exclude = ["id", "user"]
        fields = [
            "full_name",
            "phone_number",
            "street_name",
            "house_number",
            "city",
            "postal_code",
            "country"
        ]

        labels = {
            "full_name": "Full name",
            "phone_number": "Phone number",
            "street_name": "Street name",
            "house_number": "House Number",
            "city": "City",
            "postal_code": "Postal code",
            "country": "Country"
        }

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
            }),
            "country": widgets.Select(attrs={
                'class': 'form-control mb-3',
            })
        }

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]
        if not all(char.isalpha() or char.isspace() for char in full_name):
            raise ValidationError("No digits allowed in the name.")
        return full_name

    def clean_street_name(self):
        street_name = self.cleaned_data["street_name"]
        if not all(char.isalpha() or char.isspace() for char in street_name):
            raise ValidationError("Street name should only contain letters and spaces.")
        return street_name

    def clean_city(self):
        city = self.cleaned_data["city"]
        if not all(char.isalpha() or char.isspace() for char in city):
            raise ValidationError("City name should only contain letters and spaces.")
        return city
