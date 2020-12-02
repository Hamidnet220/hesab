from django.urls import path
from . import views

urlpatterns = [
    path('bank_report/<int:bank_acc_id>', views.get_bank_account_report),
]