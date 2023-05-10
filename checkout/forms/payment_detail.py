from django.forms import ModelForm, widgets, ValidationError
from checkout.models import PaymentDetails
from datetime import date, datetime


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
            "expiration_date": widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'MM/YY',
                    'data-mask': '00/00'  # Input masking pattern
                }
            ),
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
        expiration_date = self.cleaned_data['expiration_date']
        try:
            # parse the expiration date string into a datetime object
            expiration_date = datetime.strptime(expiration_date, '%m/%y')
        except ValueError:
            # raise a validation error if the date cannot be parsed correctly
            raise ValidationError("Invalid expiration date format. Please enter a valid expiration date in the format MM/YY.")

        # check that the expiration date is in the future
        if expiration_date < datetime.now():
            raise ValidationError("Expiration date must be in the future.")

        return expiration_date.strftime('%m/%y')


    def clean_cvc(self):
        cvc = self.cleaned_data["cvc"]
        if not cvc.isdigit():
            raise ValidationError("Please enter only digits for the security number.")
        if not len(cvc) == 3:
            raise ValidationError("The security number must be 3 digits long.")
        return cvc
