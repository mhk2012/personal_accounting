from datetime import date
from django.db import models

class FinancialAccount(models.Model):
    account_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100, blank=True, null=True) # Only when used is_cash equal to false
    account_number = models.CharField(max_length=50, blank=True, null=True) # Only when used is_cash equal to false
    balance = models.IntegerField(default=0)
    is_cash = models.BooleanField(default=False) # When user don't have bank account and want to create cash account

    def __str__(self):
        return f"{self.account_name} - {'Cash' if self.is_cash else self.bank_name}"
    
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    TRANSACTION_CATEGORY = [
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('housing', 'Housing'),
        ('clothing', 'Clothing'),
        ('car', 'Car'),
        ('training', 'Training'),
        ('salary', 'Salary'),
        ('sale', 'Sale'),
    ]
    
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=15, choices=TRANSACTION_CATEGORY)
    financial_account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateField(default=date.today) # Set default to today's date
    
    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"