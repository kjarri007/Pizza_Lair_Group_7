from django.forms import ModelForm, widgets
from checkout.models import PaymentDetails


class PaymentDetailsForm(ModelForm):
    class Meta:
        model = PaymentDetails
        exclude = ["id"]
        fields = [
            "card_holder",
            "card_number",
            "expiration_date",
            "cvc",
        ]
        widgets = {
            "card_holder": widgets.TextInput(attrs={'class': 'form-control'}),
            "card_number": widgets.TextInput(attrs={'class': 'form-control'}),
            "expiration_date": widgets.DateInput(attrs={'class': 'form-control'}),
            "cvc": widgets.TextInput(attrs={'class': 'form-control'}),
        }
