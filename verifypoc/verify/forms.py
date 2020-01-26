import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class EnterLivingForm(forms.Form):
    start_date = forms.DateField(
        required=True,
        help_text="Enter the date you moved in",
    )
    end_date = forms.DateField(
        required=True,
        help_text="Enter the date you moved out"
    )
    address = forms.CharField(
        required=True,
        help_text="Address of where you loved"
    )
    verifier = forms.CharField(
        required=True,
        help_text="The person to verify this"
    )

    def start_date_correct(self):
        data = self.cleaned_data['start_date']

        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - in the future'))

        return data

    def end_date_correct(self, start_date_correct):
        data = self.cleaned_data['end_date']

        if data < start_date_correct:
            raise ValidationError(_('Invalid end date - before start date'))

