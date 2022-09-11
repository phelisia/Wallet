from django import forms
from  .models import Customer,Currency,Card,Wallet,ThirdParty,Transaction,Receipts,Reward,Account,Notifications,Loan

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields ="__all__"
    
class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
        model=Currency
        fields ="__all__"   

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Card
        fields ="__all__"   


class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model=Wallet
        fields ="__all__"   

class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model=Account
        fields ="__all__"   

class ThirdpartyRegistrationForm(forms.ModelForm):
    class Meta:
        model=ThirdParty
        fields ="__all__"   

class RecieptRegistrationForm(forms.ModelForm):
    class Meta:
        model=Receipts
        fields ="__all__"   

class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Reward
        fields ="__all__"       
class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields ="__all__"   

class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model=Notifications
        fields ="__all__"    

class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields ="__all__"                                                               