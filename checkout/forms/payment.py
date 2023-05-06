from django.forms import ModelForm, fields
from checkout.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ["id"]
        fields = [
            "card_holder",
            "card_number",
            "expiration_date",
            "cvc_number"
        ]
