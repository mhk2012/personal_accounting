from django.contrib import admin
from .models import Transaction, FinancialAccount

admin.site.register(Transaction)
admin.site.register(FinancialAccount)