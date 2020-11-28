from django.shortcuts import render
from .models import BankAccount,Expens
from django.http import HttpResponse

def get_bank_account_report(request, bank_acc_id):
    expenses = Expens.objects.filter(from_bank_account__id = bank_acc_id)
    expens_str = ""
    sum_amoun = 0
    expens_str += str(BankAccount.objects.get(id = bank_acc_id))+ '<br>'

    for expens in expenses:
        expens_str += expens.desc +" | "+ '{:,}'.format(round(expens.amount),0) +" | "+ str(expens.date) + '<br>'
        sum_amoun += expens.amount

    expens_str += "جمع کل"+ " | "+ '{:,}'.format(sum_amoun) + '<br>'

    html = '<html><body>%s</body></html> ' % expens_str

    return HttpResponse(html)