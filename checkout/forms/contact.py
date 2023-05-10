from django.forms import ModelForm, widgets, ValidationError
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

        labels = {
            "full_name": "Full name",
            "phone_number": "Phone number",
            "street_name": "Street name",
            "house_number": "House Number",
            "city": "City",
            "postal_code": "Postal code"
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
            })
        }

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]
        if not all(char.isalpha() or char.isspace() for char in full_name):
            raise ValidationError("You are not Elon Musk's kid!!")
        if not len(full_name) > 3:
            raise ValidationError("You can't possibly be called that...", "Please enter a valid full name.")
        return full_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not len(str(phone_number)) == 7:
            raise ValidationError("A phone number must be exactly 7 digits long.")
        return phone_number

    def clean_street_name(self):
        street_name = self.cleaned_data["street_name"]
        if not all(char.isalpha() or char.isspace() for char in street_name):
            raise ValidationError("Street name should only contain letters and spaces.")
        return street_name

    def clean_house_number(self):
        house_number = self.cleaned_data["house_number"]
        if not len(str(house_number)) < 1 or len(str(house_number)) > 4:
            raise ValidationError("Please enter a valid house number.")
        return house_number

    def clean_city(self):
        city = self.cleaned_data["city"]
        if not all(char.isalpha() or char.isspace() for char in city):
            raise ValidationError("City name should only contain letters and spaces.")
        return city

    def clean_postal_code(self):
        postal_code = self.cleaned_data["postal_code"]
        if not len(str(postal_code)) == 3:
            raise ValidationError("Please enter a valid postal code.")
        return postal_code
