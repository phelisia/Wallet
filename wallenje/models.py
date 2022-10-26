from email.policy import default
from django.db import models
from django.forms import DateTimeField
from django.utils import timezone


# Create your models here.cxx

loan_balance=0


class Customer(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    age=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=25,null=True)
    phonenumber=models.CharField(max_length=15,null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
    date_created = models.DateTimeField(default=timezone.now)
    nationality=models.CharField(max_length=20,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)
    
    def __str__(self):
        return '{} by {}'.format(self.first_name, self.last_name,self.address,self.email,self.phonenumber,self.gender,self.age,self.profile_picture,self.date_created)

    
class Currency(models.Model):
    amount=models.IntegerField()
    country_of_origin=models.CharField(max_length=24,null=True) 

    def __str__(self):
        return '{} {}'.format(self.country_of_origin,  self.amount)


class Wallet(models.Model):
    currency =models.ForeignKey('Currency', on_delete=models.CASCADE, related_name ='Wallet_currency')
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Wallet_customer')
    balance=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=20,null=True)
    pin=models.CharField(max_length=6,null=True)

    def __str__(self):
        return '{} {}'.format(self.balance,self.currency,self.customer,self.status)

class Account(models.Model):
    account_number=models.IntegerField(default=0)
    account_type=models.CharField(max_length=20,null=True)
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Account_customer')
    balance=models.IntegerField()
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name ='Account_wallet')
    
    def __str__(self):
        return'{}{}'.format(self.balance,self.account_number,self.account_type,self.wallet,self.customer)

# DEPOSITING MONEY

    def deposit(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.balance += amount
           self.save()
           message = f"You have deposited {amount}, your new balance is {self.balance}"
           status = 200
       return message, status


# WITHDRAWING MONEY
    def withdraw(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.balance -= amount
           self.save()
           message = f"You have withdrawn {amount}, your new balance is {self.balance}"
           status = 200
       return message, status  


# REQUESTING LOAN

    def loan_request(self,amount):
        if amount <= 0:
            message =  "Invalid amount"
            status = 403
        else:
            self.loan_balance += amount
            self.balance += amount
            self.save()            
            message = f"Hello {self.customer}, You have requested for loan of  Ksh.{amount}, your new balance is {self.balance}"
            status = 200
        return message, status

# loan repayment

    def loan_repayment(self,amount):
        if amount <= 0:
            message =  "Invalid amount"
            status = 403
        else:
            self.balance -= self.loan_balance
            self.save()            
            message = f"Hello {self.customer}, Your  loan of  Ksh.{self.loan_balance} has been repayed, your new balance is {self.balance}"
            status = 200
        return message, status
    



#   buy airtime  

    def buy_airtime(self,amount):
        if amount< 0:
            message="Invalid amount"
            status=403
        else:
            self.balance += amount
            self.save()
            message=f" Hello {self.customer}, You have bought airtime for Ksh.{amount}, your new balance is {self.balance}  "
            status=200
        return message, status



# TRANSFERING MONEY

    def transfer(self, destination, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.balance -= amount
           self.save()
           destination.deposit(amount)
          
           message = f"You have transfered {amount}, your new balance is {self.balance}"
           status = 200
       return message, status

  

    

    

class Transaction(models.Model):
    transaction_ref=models.CharField(max_length=255,null=True)
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name   = 'Transaction_wallet')
    transaction_amount=models.IntegerField()
    TRANSACTION_CHOICES = (
       ('withdraw', 'Withdrawal'),
        ('depo', 'deposit'),
    )
    transaction_type=models.CharField(max_length=10, choices=TRANSACTION_CHOICES,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)
    # receipt=models.ForeignKey('Receipts',on_delete=models.CASCADE, related_name='Transaction_receipt')
    original_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_original_account')
    destination_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_destination_account')

    def __str__(self):
        return '{}{}'.format(self.transaction_type, self.destination_account,self.original_account,self.transaction_amount,self.transaction_amount)


class Card(models.Model):
    date_Issued=models.DateTimeField(default=timezone.now)
    card_name=models.CharField(max_length=20,null=True)
    card_number=models.IntegerField()
    ISSUER_CHOICES=(
         ('Master', 'Mastercard'),
        ('visa', 'visacard'),
    )
    card_type=models.CharField(max_length=10, choices=ISSUER_CHOICES,null=True)
    expiry_date=models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('d', 'debit'),
        ('c', 'credit'),
    )
    
    card_status= models.CharField(max_length=1, choices=STATUS_CHOICES,null=True)
    cvv_security=models.IntegerField()
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name ='Card_wallet')
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='Card_account')  

    def __str__(self):
        return '{} {}'.format(self.card_number,self.card_type,self.expiry_date,self.wallet,self.account,self.card_name, self.card_type)




     


class ThirdParty(models.Model):
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='ThirdParty_account')
    name=models. CharField(max_length=15,null=True)
    thirdparty_id=models.CharField(max_length=10,null=True)
    phone_Number=models.IntegerField()
    currency=models.ForeignKey('Currency', on_delete=models.CASCADE, related_name ='ThirdParty_currency')

    def __str__(self):
        return'{} {}'.format(self.account, self.name,self.thirdparty_id,self.currency,self.phone_Number)

class Notifications(models.Model):
 notification_Id=models.CharField(max_length=25,null=True)
 STATUS_CHOICES = (
        ('read', 'read'),
        ('unread', 'unread'),
    )
 status=models.CharField(max_length=12, choices=STATUS_CHOICES,null=True)
 date=models.DateTimeField(default=timezone.now)
 recipient=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Notifications_recipient')  

 def __str__(self) :
        return '{} {}'.format(self.date, self.recipient,self.status)

 

class Receipts(models.Model):
    receipt_type=models.CharField(max_length=25, null=True)
    receipt_date=models.DateTimeField(default=timezone.now)
    recipt_number=models.CharField(max_length=200, null=True)
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='Receipts_account')
    total_Amount=models.IntegerField()
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Receipts_transaction')
    recipt_File=models.FileField(upload_to='wallet/')

    def __str__(self) :
        return  '{} {}'.format(self.recipt_File,self.total_Amount,self.transaction,self.receipt_type)

    
class Loan(models.Model):
 loan_number=models.IntegerField()
 loan_type=models.CharField(max_length=25, null=True)
 amount=models.IntegerField()
 date=models.DateTimeField(default=timezone.now)
 wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name ='Loan_wallet')
 interest_rate=models.IntegerField()
 guaranter=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Loan_guaranter')
 due_date=models.DateField(default=timezone.now)
 loan_balance=models.IntegerField()
 loan_term=models.IntegerField()
     
 def __str__(self):
        return '{}{}'.format(self.loan_balance,self.loan_type,self.amount,self.guaranter,self.wallet)

 
 
 

class Reward(models.Model):  
 transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Reward_transaction')
 date=models.DateTimeField(default=timezone.now)
 customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Reward_customer')
 GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
 gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)  
 bonus=models.CharField(max_length=25, null=True)

 def __str__(self):
        return '{}{}'.format(self.transaction,self.date,self.customer,self.bonus)


 

  

    
    

    
    





   