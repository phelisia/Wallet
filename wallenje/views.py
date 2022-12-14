
from django.shortcuts import render,redirect
from rest_framework import views
from .models import Account, Card, Customer, Notifications, Reward ,Wallet,Currency,Transaction,Receipts,Loan,ThirdParty
from .forms import CustomerRegistrationForm, CurrencyRegistrationForm,CardRegistrationForm,ThirdpartyRegistrationForm,TransactionRegistrationForm,LoanRegistrationForm,RecieptRegistrationForm,RewardRegistrationForm,WalletRegistrationForm,AccountRegistrationForm,NotificationRegistrationForm

# Create your views here.
def register_customer(request):
    if request.method == 'POST':
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
              
    return render(request, 'wallet/register_customer.html',{'form':form})

def list_customers(request):
        customers=Customer.objects.all()
        return render(request, 'wallet/customer_list.html',{'customers':customers})

def register_currency(request):
    form=CurrencyRegistrationForm()
    return render(request, 'wallet/register_currency.html',{'form':form})    


def list_currency(request):
    currencys=Currency.objects.all()
    return render(request, 'wallet/currency_list.html',{'currency_list':currencys})

def register_card(request):
    form=CardRegistrationForm()
    return render(request, 'wallet/register_card.html',{'form':form})


def list_card(request):
    cards=Card.objects.all()
    return render(request, 'wallet/card_list.html',{'card_list':cards})


def register_Transaction(request):
    form=TransactionRegistrationForm()
    return render(request, 'wallet/register_transaction.html',{'form':form})   


def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request, 'wallet/transaction_list.html',{'transaction_list':transactions})


def register_account(request):
    form=AccountRegistrationForm()
    return render(request, 'wallet/register_account.html',{'form':form})

def list_account(request):
    accounts=Account.objects.all()
    return render(request, 'wallet/account_list.html',{'account_list':accounts})


def register_loan(request):
    form=LoanRegistrationForm()
    return render(request, 'wallet/registration_loan.html',{'form':form})


def list_loan(request):
    loans=Loan.objects.all()
    return render(request, 'wallet/loan_list.html',{'loans':loans})



def register_wallet(request):
    form=WalletRegistrationForm()
    return render(request, 'wallet/register_wallet.html',{'form':form})


def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request, 'wallet/wallet_list.html',{'wallets':wallets})


def register_notifications(request):
    form=NotificationRegistrationForm()
    return render(request, 'wallet/register_notifications.html',{'form':form})


def list_notifications(request):
    notifications=Notifications.objects.all()
    return render(request, 'wallet/notifications_list.html',{'notifications_list':notifications})



def register_thirdparty(request):
    form=ThirdpartyRegistrationForm()
    return render(request, 'wallet/register_thirdparty.html',{'form':form})


def list_thirdparty(request):
        thirdpartys=ThirdParty.objects.all()
        return render(request, 'wallet/thirdparty_list.html',{'thirdparty_list':thirdpartys})


def register_reward(request):
    form=RewardRegistrationForm()
    return render(request, 'wallet/register_reward.html',{'form':form})  



def list_rewards(request):
    rewards=Reward.objects.all()
    return render(request, 'wallet/rewards_list.html',{'rewards_list':rewards})


def register_receipt(request):
    form=RecieptRegistrationForm()
    return render(request, 'wallet/register_receipts.html',{'form':form})      


def list_receipts(request):
    receiptss=Receipts.objects.all()
    return render(request, 'wallet/receipts_list.html',{'receiptss':receiptss})


def wallet_profile(request,id):
    wallets=Wallet.objects.get(id=id)
    return render(request, 'wallet/wallet_profile.html',{'wallets':wallets})


def customer_profile(request,id):
    customer=Customer.objects.get(id=id)
    return render(request, 'wallet/customer_profile.html',{'customer':customer})   

def account_profile(request,id):
    account=Account.objects.get(id=id)
    return render(request, 'wallet/account_profile.html',{'account':account})        

def transaction_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    return render(request, 'wallet/transaction_profile.html',{'transaction':transaction})

def customer_profile(request,id):
    customer=Customer.objects.get(id=id)
    return render(request, 'wallet/customer_profile.html',{'customer':customer})   


def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render(request, 'wallet/card_profile.html',{'card':card}) 


def receipt_profile(request,id):
    receipt=Receipts.objects.get(id=id)
    return render(request, 'wallet/receipt_profile.html',{'receipt':receipt})                    


def edit_customer(request,id):
   customer = Customer.objects.get(id=id)
   if request.method == 'POST':

        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return  redirect("customer_profile", id = customer.id)
   else:
            form = CustomerRegistrationForm(instance=customer)
   return render(request, "wallet/edit_customer.html", {'form':form})


def edit_transaction(request,id):
   transaction = Transaction.objects.get(id=id)
   if request.method == 'POST':

        form = TransactionRegistrationForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return  redirect("edit_transaction", id = transaction.id)
   else:
            form = TransactionRegistrationForm(instance=transaction)
   return render(request, "wallet/edit_transaction.html", {'form':form})   



def edit_card(request,id):
   card= Card.objects.get(id=id)
   if request.method == 'POST':

        form = CardRegistrationForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return  redirect("edit_card", id = card.id)
   else:
            form = CardRegistrationForm(instance=card)
   return render(request, "wallet/edit_card.html", {'form':form})


def edit_receipt(request,id):
   receipt= Receipts.objects.get(id=id)
   if request.method == 'POST':

        form = RecieptRegistrationForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            return  redirect("edit_receipt", id = receipt.id)
   else:
            form = RecieptRegistrationForm(instance=receipt)
   return render(request, "wallet/edit_receipt.html", {'form':form})        




def edit_wallet(request,id):
   wallet= Wallet.objects.get(id=id)
   if request.method == 'POST':

        form = WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return  redirect("edit_wallet", id = wallet.id)
   else:
            form = WalletRegistrationForm(instance=wallet)
   return render(request, "wallet/edit_wallet.html", {'form':form})  


def edit_account(request,id):
   account= Account.objects.get(id=id)
   if request.method == 'POST':

        form = AccountRegistrationForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return  redirect("edit_account", id = account.id)
   else:
            form = AccountRegistrationForm(instance=account)
   return render(request, "wallet/edit_account.html", {'form':form})         





 