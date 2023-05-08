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
            "postal_code"
        ]
        widgets = {
            "full_name": widgets.TextInput(attrs={'class': 'form-control'}),
            "phone_number": widgets.TextInput(attrs={'class': 'form-control'}),
            "street_name": widgets.TextInput(attrs={'class': 'form-control'}),
            "house_number": widgets.TextInput(attrs={'class': 'form-control'}),
            "city": widgets.TextInput(attrs={'class': 'form-control'}),
            "postal_code": widgets.TextInput(attrs={'class': 'form-control'})
        }
