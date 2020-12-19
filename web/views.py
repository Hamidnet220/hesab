from django.db.models import Sum, F
from django.shortcuts import render,redirect
from django.http import HttpResponse

from jdatetime import JalaliToGregorian
from datetime import date

from .models import BankAccount, Transaction, TransCategory

def home_view(request):
    
    return render(request,'home.html',{})

def get_bank_account_report(request):

     
    banks_accounts = BankAccount.objects.all()

    if request.method == "POST":
        start_date = request.POST['start-date'].split('/')
        end_date = request.POST['end-date'].split('/')

        start_date = list(map(lambda item: int(item),start_date))
        end_date = list(map(lambda item: int(item),end_date))
        
        start_date = JalaliToGregorian(start_date[0],start_date[1],start_date[2]).getGregorianList()
        end_date = JalaliToGregorian(end_date[0],end_date[1],end_date[2]).getGregorianList()

        start_date = date(start_date[0],start_date[1],start_date[2])
        end_date = date(end_date[0],end_date[1],end_date[2])
        

        bank_select = BankAccount.objects.filter(account_number=request.POST['bank_accounts'])[0]
        initial_balance = BankAccount.objects.get(id=bank_select.id).initial_balance
        trans = Transaction.objects.filter(bank_account__id = bank_select.id).filter(date__gte=start_date).filter(date__lte=end_date).order_by('date')

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
        print(total_amount)
        trans= zip(trans,remains)


        contents = {
            'trans' : trans,
            'total_amount' : total_amount,
            'bank_accounts':banks_accounts,

        }

        return render(request,"bank_account_report.html", contents)

    else:
       
        contents = {
        'bank_accounts':banks_accounts,
        }

        return render(request,"bank_account_report.html",contents)

def get_category_expens_amount(request):
    expens_cat = TransCategory.objects.filter(category_type=1).values('title').annotate(cat_sum=Sum('transaction__amount'))
    total_amount = expens_cat.aggregate(Sum('cat_sum'))
    
    contents = {
        'expens_cat' : expens_cat,
        'total_amount':total_amount,
    }

    return render(request,'expens_category_report.html',contents)
    



def transfer_amount(request):

    bank_accounts = BankAccount.objects.all()
    

    contents = {
        'bank_accounts' : bank_accounts,
    }
    return render(request, "transfer_amount.html", contents)