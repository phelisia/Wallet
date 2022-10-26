from django.db import router
from django.urls import path,include
from rest_framework import routers

from wallenje.views import AccountDepositView
from  .views import AccountViewSet, CardViewSet, CustomerViewSet, LoanViewSet, NotificationViewSet, ReceiptsViewSet, TransactionViewSet, WalletViewSet

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
]