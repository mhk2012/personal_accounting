from django.shortcuts import render, redirect
from .models import FinancialAccount, Transaction
from .forms import FinancialAccountForm, TransactionForm

def index(request):
    transactions = Transaction.objects.all()
    financial_accounts = FinancialAccount.objects.all()

    total_income = sum(t.amount for t in transactions if t.transaction_type == 'income')
    total_expense = sum(t.amount for t in transactions if t.transaction_type == 'expense')
    balance = total_income - total_expense

    return render(request, 'index.html', {
        'transactions': transactions,
        'financial_accounts': financial_accounts,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance
        })

def add_financial_account(request):
    if request.method == 'POST':
        form = FinancialAccountForm(request.POST)
        if form.is_valid():
            financial_account = form.save(commit=False)
            financial_account.save()
            return redirect('index')
    else:
        form = FinancialAccountForm()
    return render(request, 'add_financial_account.html', {'form': form})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.save()
            return redirect('index')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})
