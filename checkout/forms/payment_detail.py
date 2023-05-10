from django.forms import ModelForm, widgets, ValidationError
from checkout.models import PaymentDetails
from django.utils import timezone
from datetime import datetime, timezone


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

        labels = {
            "card_holder": "Full Name",
            "card_number": "Card Number",
            "expiration_date": "Exp.Date",
            "cvc": "CVC"
        }

    @staticmethod
    def clean_card_number(self):
        card_number = PaymentDetails.card_number
        if not card_number.isdigit():
            raise ValidationError("Please enter only digits.")
        if not len(card_number) == 16:
            raise ValidationError("A credit card number must be exactly 16 digits long.")
        return card_number

    @staticmethod
    def clean_expiration_date(self):
        expiration_date = datetime.strptime(str(PaymentDetails.expiration_date), "%m-%y")
        today = timezone.now()
        if not expiration_date < today:
            raise ValidationError("This is not a valid expiration date.")
        return expiration_date
