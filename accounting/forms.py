from django import forms
from .models import FinancialAccount, Transaction

class FinancialAccountForm(forms.ModelForm):
    class Meta:
        model = FinancialAccount
        fields = ['account_name', 'bank_name', 'account_number', 'balance', 'is_cash']
        widgets = {
            'account_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_cash': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        is_cash = cleaned_data.get('is_cash')
        bank_name = cleaned_data.get('bank_name')
        account_number = cleaned_data.get('account_number')

        if is_cash:
            # Don't need to show an error, just empty the 'bank_name' and 'account_number'
            cleaned_data['bank_name'] = ''
            cleaned_data['account_number'] = ''
        else:
            if not bank_name:
                self.add_error('bank_name', 'This field is required.')
            if not account_number:
                self.add_error('account_number', 'This field is required.')

        return cleaned_data

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'category', 'financial_account', 'amount', 'date']
        widgets = {
            'transaction_type': forms.Select(attrs={'class': 'form-select'}), 
            'category': forms.Select(attrs={'class': 'form-select'}), 
            'financial_account': forms.Select(attrs={'class': 'form-select'}), 
            'amount': forms.NumberInput(attrs={'class': 'form-control'}), 
            'date': forms.DateInput(attrs={'class': 'form-control'}), 
        }

class ReportForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True,
        label='Start Date'
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True,
        label='End Date'
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            self.add_error('end_date', 'End date should be greater than start date.')

        return cleaned_data