from django.forms import ModelForm, widgets
from checkout.models import SecondInfoWindow


class SecondInfoWindowForm(ModelForm):
    class Meta:
        model = SecondInfoWindow
        exclude = ["id"]
        fields = [
            "name",
            "number",
            "date",
            "secret_number",
        ]
        widgets = {
            "name": widgets.TextInput(attrs={'class': 'form-control'}),
            "number": widgets.TextInput(attrs={'class': 'form-control'}),
            "date": widgets.TextInput(attrs={'class': 'form-control'}),
            "secret_number": widgets.TextInput(attrs={'class': 'form-control'}),
        }
