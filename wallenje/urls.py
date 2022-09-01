from django.urls import path
from.views import register_customer, register_currency,register_account,register_card,register_loan,register_Transaction, register_notifications, register_receipt,register_thirdparty, register_wallet,register_reward,register_loan
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

]
