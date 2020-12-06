from django.db.models import Sum, F

from django.shortcuts import render
from django.http import HttpResponse

from .models import BankAccount, Transaction, TransCategory



def get_bank_account_report(request, bank_acc_id = 1):

    initial_balance = BankAccount.objects.get(id=bank_acc_id).initial_balance
    
    trans = Transaction.objects.filter(bank_account__id = bank_acc_id).order_by('date')

    remains = []
    curren_balance = initial_balance
    for tran in trans:
        if tran.transaction_type == 1:
            curren_balance = curren_balance + tran.amount
            remains.append(curren_balance)
        elif tran.transaction_type == 2:
            curren_balance = curren_balance - tran.amount
            remains.append(curren_balance)

    total_amount = trans.filter(transaction_type=1).aggregate(Sum('amount'))

    trans= zip(trans,remains)
    
    


    contents = {
        'trans' : trans,
        'total_amount' : total_amount,
    }

    return render(request,"bank_account_report.html", contents)

def get_category_expens_amount(request):
    expens_cat = TransCategory.objects.filter(category_type=1).values('title').annotate(cat_sum=Sum('transaction__amount'))
    
    contents = {
        'expens_cat' : expens_cat,
    }

    return render(request,'expens_category_report.html',contents)
    



def transfer_amount(request):

    bank_accounts = BankAccount.objects.all()
    

    contents = {
        'bank_accounts' : bank_accounts,
    }
    return render(request, "transfer_amount.html", contents)