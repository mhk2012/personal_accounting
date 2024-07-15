from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import FinancialAccount, Transaction
from .forms import FinancialAccountForm, TransactionForm, ReportForm

def index(request):
    transactions = Transaction.objects.all()
    financial_accounts = FinancialAccount.objects.all()

    total_income = sum(t.amount for t in transactions if t.transaction_type == 'income')
    total_expense = sum(t.amount for t in transactions if t.transaction_type == 'expense')
    total_balance = total_income - total_expense

    account_balances = {}
    for account in financial_accounts:
        account_transactions = transactions.filter(financial_account=account)
        income = sum(t.amount for t in account_transactions if t.transaction_type == 'income')
        expense = sum(t.amount for t in account_transactions if t.transaction_type == 'expense')
        account_balances[account] = income - expense + account.balance

    return render(request, 'index.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'total_balance': total_balance,
        'account_balances': account_balances,
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

def generate_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            transactions = Transaction.objects.filter(date__range=[start_date, end_date])

            total_income = sum(t.amount for t in transactions if t.transaction_type == 'income')
            total_expense = sum(t.amount for t in transactions if t.transaction_type == 'expense')
            balance = total_income - total_expense

            return render(request, 'report_results.html', {
                'form': form,
                'transactions': transactions,
                'start_date': start_date,
                'end_date': end_date,
                'total_income': total_income,
                'total_expense': total_expense,
                'balance': balance
            })
    else:
        form = ReportForm()

    return render(request, 'report.html', {'form': form})

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Transaction deleted successfully.')
        return redirect('index')
    return render(request, 'delete_transaction.html', {'transaction': transaction})