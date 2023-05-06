from django.forms import ModelForm, fields
from . import Payment

from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from creditcards import types


class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')

    assert types.get_type('4444333322221111') == types.CC_TYPE_VISA
    assert types.get_type('343434343434343') == types.CC_TYPE_AMEX
    assert types.get_type('0000000000000000') == types.CC_TYPE_GENERIC


class Payment(ModelForm):
    cardholder = fields.CharField(max_length=100),
    card_number = fields.IntegerField(max_value=16, min_value=16),
    
    class Meta:
        model = Payment
        exclude = ["id", "user"]
        fields = {
            "cardholder": fields.CharField(max_length=100),
            "card_number": fields.IntegerField(),
            "expiration_date": fields.DateField(),
            "cvc": fields.IntegerField()
            # "image": widgets.TextInput(attrs={"class": "form-control"})
        }
