from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import *
router=routers.DefaultRouter()
router.register('customers',CustomerViewSet)
router.register('wallets',WalletViewSet)
router.register('cards',CardViewSet)
router.register('accounts',AccountViewSet)
router.register('notifications',NotificationViewSet)
router.register('transactions',TransactionViewSet)
router.register('loan',LoanViewSet)
router.register('receipt',ReceiptsViewSet)
urlpatterns=[
path('',include(router.urls)),
path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
path("deposit/<int:id>",AccountDepositView.as_view(),name='deposit-view'), 
path("transfer/<int:pk>/",AccountTransferView.as_view(), name="transfer-view"),
path("withdrawal/",AccountWithdrawalView.as_view(),name="withrawal-view"),
path("loan_request/",AccountLoanRequestView.as_view(),name="loan-view"),
path("loan_repayment/",AccountLoanRepaymentView.as_view(),name="repay-loan-view"),
path("buy_airtime/",AccountBuyAirtimeView.as_view(),name="repay-loan-view")

]