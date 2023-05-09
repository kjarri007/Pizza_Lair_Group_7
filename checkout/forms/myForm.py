from django.forms import ModelForm, widgets
from checkout.models import MyStory


class myForm(ModelForm):
    class Meta:
        model = MyStory
        exclude = ["id"]
        fields = [
            "mammaþin",
            "eitthvad",
            "koolbro",
            "okok",
        ]
        widgets = {
            "mammaþin": widgets.TextInput(attrs={'class': 'form-control'}),
            "eitthvad": widgets.TextInput(attrs={'class': 'form-control'}),
            "koolbro": widgets.DateInput(attrs={'class': 'form-control'}),
            "okok": widgets.TextInput(attrs={'class': 'form-control'}),
        }
