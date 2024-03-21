from django.http import JsonResponse
from django.views.generic import View
from .models import Account, Transaction
import json

class AccountListView(View):
    def get(self, request):
        accounts = Account.objects.all()
        data = [{'account_number': account.account_number, 'account_type': account.account_type, 'balance': account.balance, 'client_id': account.client_id} for account in accounts]
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            new_account = Account.objects.create(account_type=data['account_type'], balance=data['balance'], client_id=data['client_id'])
            response_data = {'account_number': new_account.account_number, 'account_type': new_account.account_type, 'balance': new_account.balance, 'client_id': new_account.client_id}
            return JsonResponse(response_data, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class AccountDetailView(View):
    def get(self, request, account_number):
        try:
            account = Account.objects.get(account_number=account_number)
            data = {'account_number': account.account_number, 'account_type': account.account_type, 'balance': account.balance, 'client_id': account.client_id}
            return JsonResponse(data)
        except Account.DoesNotExist:
            return JsonResponse({'error': 'Account not found'}, status=404)

    def put(self, request, account_number):
        try:
            account = Account.objects.get(account_number=account_number)
            data = json.loads(request.body)
            account.account_type = data.get('account_type', account.account_type)
            account.balance = data.get('balance', account.balance)
            account.client_id = data.get('client_id', account.client_id)
            account.save()
            response_data = {'account_number': account.account_number, 'account_type': account.account_type, 'balance': account.balance, 'client_id': account.client_id}
            return JsonResponse(response_data)
        except Account.DoesNotExist:
            return JsonResponse({'error': 'Account not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, account_number):
        try:
            account = Account.objects.get(account_number=account_number)
            account.delete()
            return JsonResponse({'message': 'Account deleted successfully'})
        except Account.DoesNotExist:
            return JsonResponse({'error': 'Account not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class TransactionListView(View):
    def get(self, request):
        transactions = Transaction.objects.all()
        data = [{'id': transaction.id, 'account_id': transaction.account_id, 'transaction_type': transaction.transaction_type, 'amount': transaction.amount, 'date': transaction.date} for transaction in transactions]
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            new_transaction = Transaction.objects.create(account_id=data['account_id'], transaction_type=data['transaction_type'], amount=data['amount'])
            response_data = {'id': new_transaction.id, 'account_id': new_transaction.account_id, 'transaction_type': new_transaction.transaction_type, 'amount': new_transaction.amount, 'date': new_transaction.date}
            return JsonResponse(response_data, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class TransactionDetailView(View):
    def get(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            data = {'id': transaction.id, 'account_id': transaction.account_id, 'transaction_type': transaction.transaction_type, 'amount': transaction.amount, 'date': transaction.date}
            return JsonResponse(data)
        except Transaction.DoesNotExist:
            return JsonResponse({'error': 'Transaction not found'}, status=404)

    def put(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            data = json.loads(request.body)
            transaction.account_id = data.get('account_id', transaction.account_id)
            transaction.transaction_type = data.get('transaction_type', transaction.transaction_type)
            transaction.amount = data.get('amount', transaction.amount)
            transaction.save()
            response_data = {'id': transaction.id, 'account_id': transaction.account_id, 'transaction_type': transaction.transaction_type, 'amount': transaction.amount, 'date': transaction.date}
            return JsonResponse(response_data)
        except Transaction.DoesNotExist:
            return JsonResponse({'error': 'Transaction not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            transaction.delete()
            return JsonResponse({'message': 'Transaction deleted successfully'})
        except Transaction.DoesNotExist:
            return JsonResponse({'error': 'Transaction not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

