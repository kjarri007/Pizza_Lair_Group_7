from django.forms import ModelForm, widgets

from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["id", "user"]
        fields = [
            "image",
            "full_name",
            "phone_number",
            "street_name",
            "house_number",
            "city",
            "postal_code",
        ]

        widgets = {
            "image": widgets.TextInput(attrs={
                "class": "form-control",
                "type": "file"
            }),
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
