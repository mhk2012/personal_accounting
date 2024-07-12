from django import forms
from .models import FinancialAccount, Transaction

class FinancialAccountForm(forms.ModelForm):
    class Meta:
        model = FinancialAccount
        fields = ['account_name', 'bank_name', 'account_number', 'balance', 'is_cash']

    def clean(self):
        cleaned_data = super().clean()
        is_cash = cleaned_data.get('is_cash')
        bank_name = cleaned_data.get('bank_name')
        account_number = cleaned_data.get('account_number')

        if is_cash:
            if bank_name or account_number:
                raise forms.ValidationError("Bank name and account number should be empty for cash accounts.")
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