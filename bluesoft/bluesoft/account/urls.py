from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.urls import path
from .views import AccountListView,AccountDetailView,TransactionListView,TransactionDetailView
urlpatterns = [
    path('view',AccountListView.as_view()),
    path('details/<int:account_number>',AccountDetailView.as_view()),
    path('transaction/view',TransactionListView.as_view()),
    path('transaction/details/<int:transaction_id>',TransactionDetailView.as_view()),
]
