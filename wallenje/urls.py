from django.urls import path
from.views import list_account, list_card, list_currency, list_customers, list_loan, list_notifications, list_receipts, list_rewards, list_thirdparty, list_transaction, list_wallet, register_customer, register_currency,register_account,register_card,register_loan,register_Transaction, register_notifications, register_receipt,register_thirdparty, register_wallet,register_reward,register_loan
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
    path("customer_list",list_customers,name='customer_list'), 
    path("account_list",list_account,name='customer_list'),
    path("card_list",list_card,name='customer_list'), 
    path("currency_list",list_currency,name='customer_list'), 
    path("loan_list",list_loan,name='customer_list'), 
    path("notifications_list",list_notifications,name='customer_list'), 
    path("reward_list",list_rewards,name='customer_list'), 
    path("thirdparty_list",list_thirdparty,name='customer_list'), 
    path("transaction_list",list_transaction,name='customer_list'), 
    path("wallet_list",list_wallet,name='customer_list'),  

]
