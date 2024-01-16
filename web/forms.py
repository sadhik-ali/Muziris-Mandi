# web/forms.py
from django import forms
from django.forms import widgets

from .models import Contact


class Contact(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Name"}
            ),
            "phone": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Phone"}
            ),
            "subject": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your subject"}
            ),
            "email": widgets.EmailInput(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Your Email Address",
                }
            ),
            "message": widgets.Textarea(
                attrs={
                    "class": "required form-control",
                    "placeholder": "Type Your Message",
                }
            ),
        }
