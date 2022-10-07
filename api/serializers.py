from rest_framework import serializers
from wallenje.models import Account, Card, Customer, Loan, Notifications, Receipts, Transaction ,Wallet


class CustomerSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name','last_name',)



class WalletSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('currency','customer','balance','amount','status','pin','date',)        


class CardSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('card_name','date_Issued','card_number','card_type','expiry_date','card_status','cvv_security','wallet','account')       




class AccountSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_number','account_type','balance','name','wallet',)                       





class TransactionSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_ref','wallet','transaction_ref','transaction_type','transaction_charge','transaction_date','original_account','destination_account',)     




class LoanSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('loan_number','loan_type','balance','walllet','intrest_rate','pin','guaranter','due_date','loan_balance','loan_term',)      



class ReceiptSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Receipts
        fields = ('receipt_type','receipt_date','recipt_number','recipt_File','transaction','total_Amount','account',)        





class NotificationsSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ('notification_Id','date','status','recipient',)                                         