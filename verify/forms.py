import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Profile, Businesses, LivingItem


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
    verifier = forms.ModelChoiceField(
        queryset=Businesses.objects.all().order_by('business_name')
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


class EnterWorkForm(forms.Form):
    start_date = forms.DateField(
        required=True,
        help_text="Enter the date you moved in",
    )
    end_date = forms.DateField(
        required=True,
        help_text="Enter the date you moved out"
    )
    work_place = forms.CharField(
        required=True,
        help_text="The place where you worked"
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


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'birth_date')


class RequesterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email',)

    def save(self):
        user = super().save(commit=False)
        user.is_requester = True
        user.save()
        return user


class VerifierSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email',
                  'business_type', 'business_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_verifier = True
        if commit:
            user.save()
        return user


class ShareWithForm(forms.Form):
    share_with = forms.ModelChoiceField(queryset=Businesses.objects.all())
