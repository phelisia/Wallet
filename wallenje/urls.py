from django.urls import path
from .views import * 
urlpatterns=[
    path("",register_customer,name='registration'),
    path("currency/",register_currency,name='currency'),
    path("card/",register_card,name='card'),
    path("account/",register_account,name='accout'),
    path("wallet/",register_wallet,name='wallet'),
    path("reward/",register_reward,name='reward'),
    path("receipt/",register_receipt,name='receipt'),
    path("transaction/",register_Transaction,name='transaction'),
    path("loan/",register_loan,name='loan'),
    path("notification/",register_notifications,name='notification'),
    path("thirdparty/",register_thirdparty,name='thirdparty'),
    path("customers",list_customers,name='customer_list'), 
    path("accounts",list_account,name='customer_list'),
    path("cards",list_card,name='customer_list'), 
    path("currency_list",list_currency,name='customer_list'), 
    path("loan_list",list_loan,name='customer_list'), 
    path("notifications_list",list_notifications,name='customer_list'), 
    path("reward_list",list_rewards,name='customer_list'), 
    path("thirdparty_list",list_thirdparty,name='customer_list'), 
    path("transactions",list_transaction,name='transaction_list'), 
    path("wallets",list_wallet,name='wallet_list'),  
    path("receipts",list_receipts,name='customer_list'),
    path("customers/<int:id>",customer_profile,name='customer_profile'), 
    path("transactions/<int:id>",transaction_profile,name='transaction_profile'), 
    path("cards/<int:id>",card_profile,name='wallet_profile'), 
    path("accounts/<int:id>",account_profile,name='account_profile'), 
    path("customers/edit/<int:id>",edit_customer,name='edit_customer'),
    path("wallets/<int:id>",wallet_profile,name='wallet_profile'), 
    path("receipts/<int:id>",receipt_profile,name='receipt_profile'), 
    path("transactions/edit/<int:id>",edit_transaction,name='edit_transaction'),
    path("cards/edit/<int:id>",edit_card,name='edit_card'),
    path("receipts/edit/<int:id>",edit_receipt,name='edit_receipts'),
    path("accounts/edit/<int:id>",edit_account,name='edit_account'),
    path("wallets/edit/<int:id>",edit_wallet,name='edit_wallet'),
   
  
     



]
