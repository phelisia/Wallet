
from django.contrib import admin
from .models import Customer,Wallet,Currency,Transaction,Card,ThirdParty ,Receipts,Loan,Reward,Notifications,Account
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email','address','gender','profile_picture',)
    search_fields=('first_name','last_name',)

admin.site.register(Customer,CustomerAdmin)



class ReceiptsAdmin(admin.ModelAdmin):
    list_display=('receipt_type','receipt_date','recipt_number','account','total_Amount','transaction','recipt_File',)
    search_fields=('recipt_File','recipt_number',)   

admin.site.register(Receipts,ReceiptsAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_ref','wallet','transaction_type','transaction_charge','original_account','destination_account',)
    search_fields=('transaction_ref','transaction_amount',)
admin.site.register(Transaction,TransactionAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display=('date_Issued','card_name','card_number','card_type','expiry_date','card_status','cvv_security','account',)
    search_fields=('date_Issued','card_name',)
admin.site.register(Card,CardAdmin)


class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=('name','account','thirdparty_id','phone_Number','currency',)
    search_fields=('name','thirdparty_id',)
admin.site.register(ThirdParty,ThirdPartyAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=('amount','country_of_origin',)
    search_fields=('country_of_origin','amount',)
admin.site.register(Currency,CurrencyAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display=('currency','customer','balance','amount','date','status','pin',)
    search_fields=('customer','balance',)
admin.site.register(Wallet,WalletAdmin)


class RewardAdmin(admin.ModelAdmin):
    list_display=('transaction','date','customer','bonus',)
    search_fields=('bonus','customer',)
admin.site.register(Reward,RewardAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_number','loan_type','amount','date','wallet','interest_rate','guaranter','due_date','loan_balance','loan_term',)
    search_fields=('loan_type','wallet',)
admin.site.register(Loan,LoanAdmin)


class NotificationsAdmin(admin.ModelAdmin):
    list_display=('status','date','recipient',)
    search_fields=('recipient','status',)
admin.site.register(Notifications,NotificationsAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display=('account_number','account_type','balance','wallet','customer',)
    search_fields=('account_number','customer',)
admin.site.register(Account,AccountAdmin)
 

