from django.forms import ModelForm, widgets, ValidationError
from checkout.models import PaymentDetails
from django.utils import timezone
from datetime import datetime, date
import re


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

    def clean_card_holder(self):
        card_holder = self.cleaned_data["card_holder"]
        if not all(char.isalpha() or char.isspace() for char in card_holder):
            raise ValidationError("You are not Elon Musk's kid!!")
        if not len(card_holder) > 3:
            raise ValidationError("You can't possibly be called that...")
        return card_holder

    def clean_card_number(self):
        card_number = self.cleaned_data["card_number"]
        if not card_number.isdigit():
            raise ValidationError("Please enter only digits in card number.")
        if not len(card_number) == 16:
            raise ValidationError("A credit card number must be exactly 16 digits long.")
        return card_number

    def clean_expiration_date(self):
        # expiration_date = self.cleaned_data.get('expiration_date')
        # # Validate the format "MM/YY" using regex
        # if not re.match(r'^\d{2}/\d{2}$', expiration_date):
        #     raise ValidationError("Invalid expiration date format. Please use MM/YY format.")
        # # Extract the month and year from the input
        # month, year = expiration_date.split('/')
        # # Validate the month and year values
        # current_year = date.today().year % 100
        # if not (1 <= int(month) <= 12 and int(year) >= current_year):
        #     raise ValidationError("Invalid expiration date.")
        # return expiration_date
        today = date.today()
        expiration_date = self.cleaned_data["expiration_date"]
        if not expiration_date > today:
            raise ValidationError("This card is expired.")
        return expiration_date

    def clean_cvc(self):
        cvc = self.cleaned_data["cvc"]
        if not cvc.isdigit():
            raise ValidationError("Please enter only digits for the security number.")
        if not len(cvc) == 3:
            raise ValidationError("The security number must be 3 digits long.")
        return cvc
