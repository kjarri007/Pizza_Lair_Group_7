from django.forms import ModelForm, fields
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
