from django.urls import path
from . import views

urlpatterns = [
    path('bank_report/<int:bank_acc_id>', views.get_bank_account_report, name='bank_report'),
    path('category_report', views.get_category_expens_amount, name='category_report'),
    
]