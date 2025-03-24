from django import forms
from .models import Booking, Facility

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['facility', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        facility = cleaned_data.get('facility')
        date = cleaned_data.get('date')

        if facility and date:
            if Booking.objects.filter(facility=facility, date=date).exists():
                raise forms.ValidationError(
                    "This facility is already booked for the selected date."
                )
        return cleaned_data
