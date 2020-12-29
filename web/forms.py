from django import forms
from .models import Transaction

from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
