from django.forms import ModelForm, fields
from user.models import ContactInfo


class ContactInfo(ModelForm):
    class Meta:
        model = ContactInfo
        exclude = ["id", "user"]
        fields = {
            "name": fields.CharField(),
            "street_name": fields.CharField(),
            "house_number": fields.IntegerField(),
            "city": fields.CharField(),
            # "country": fields.CharField(),
            "postal_code": fields.IntegerField()
            # "image": widgets.TextInput(attrs={"class": "form-control"})
        }
