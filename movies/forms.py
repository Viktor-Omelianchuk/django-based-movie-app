from django import forms

from .models import Reviews, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    """Feedback form"""

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class RatingForm(forms.ModelForm):
    """Rating add form"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)