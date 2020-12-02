from django.db.models import Sum, F

from django.shortcuts import render
from django.http import HttpResponse

from .models import BankAccount,Expens



def get_bank_account_report(request, bank_acc_id = 1):
    
    Expens.objects.annotate(total_amounts = Sum(F('amount')))
    expenses = Expens.objects.filter(from_bank_account__id = bank_acc_id).order_by('-date')

    bank_account = BankAccount.objects.get(id=bank_acc_id)

    contents = {
        'expenses' : expenses,
        'bank_account' : bank_account,
    }

    return render(request,"bank_account_report.html", contents)


def transfer_amount(request):

    bank_accounts = BankAccount.objects.all()
    

    contents = {
        'bank_accounts' : bank_accounts,
    }
    return render(request, "transfer_amount.html", contents)