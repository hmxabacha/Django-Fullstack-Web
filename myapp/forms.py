from .models import BookingModel
from django import forms

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = BookingModel
        fields = "__all__"
