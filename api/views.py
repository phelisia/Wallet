from django import views
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from wallenje .models import Account, Card, Customer, Loan, Notifications, Receipts, Transaction,Wallet
from .serializers import AccountSerilaizers, CardSerilaizers, CustomerSerilaizers, LoanSerilaizers, NotificationsSerilaizers, ReceiptSerilaizers, TransactionSerilaizers, WalletSerilaizers


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class= CustomerSerilaizers


class WalletViewSet(viewsets.ModelViewSet):
    queryset=Wallet.objects.all()
    serializer_class= WalletSerilaizers    


class CardViewSet(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class= CardSerilaizers    



class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class= AccountSerilaizers    



class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class= TransactionSerilaizers    



class ReceiptsViewSet(viewsets.ModelViewSet):
    queryset=Receipts.objects.all()
    serializer_class= ReceiptSerilaizers    



class LoanViewSet(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class= LoanSerilaizers         



class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notifications.objects.all()
    serializer_class= NotificationsSerilaizers       





class AccountDepositView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)    
                
