from django import forms
from .models import FinancialAccount, Transaction

class FinancialAccountForm(forms.ModelForm):
    class Meta:
        model = FinancialAccount
        fields = ['account_name', 'bank_name', 'account_number', 'balance', 'is_cash']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'category', 'financial_account', 'amount', 'date']