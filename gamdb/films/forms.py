from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class CommentForm(forms.Form):
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Jméno"})
    )
    text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 5, "class": "form-control", "placeholder" : "komentář..."})
    )
    rating = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder" : "X%"}),
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
