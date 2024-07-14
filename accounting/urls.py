from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_financial_account', views.add_financial_account, name='add_financial_account'),
    path('add_transaction', views.add_transaction, name='add_transaction'),
    path('report', views.generate_report, name='generate_report'),
]
