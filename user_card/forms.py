from django import forms
from .models import CardImage


class CardImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = CardImage
        fields = ('id', 'front_img', 'back_img',)