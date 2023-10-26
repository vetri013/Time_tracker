from django import forms
from .models import TimeEntry

class TimeEntryForm (forms.ModelForm):
    class Meta:
        model=TimeEntry
        fields=['date','hours_worked','description']