from django.contrib import admin
from .models import BankAccount, Expens, Income, IncomeCategory, ExpensCategory

admin.site.register(ExpensCategory)
admin.site.register(IncomeCategory)




@admin.register(Expens)
class ExpensAdmin(admin.ModelAdmin):
    list_display = ('category', 'desc', 'format_to_thous_sep', 'date',)
    list_filter = ('category',)
    ordering = ['-date'] 

    def format_to_thous_sep(self, obj):
        return '{:,}'.format(round(obj.amount,0))
    format_to_thous_sep.short_description = "مبلغ (ریال)"



@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('category', 'desc', 'format_to_thous_sep', 'date',)
    list_filter = ('category',)
    ordering =['-date']

    def format_to_thous_sep(self, obj):
        return '{:,}'.format(round(obj.amount,0))
    format_to_thous_sep.short_description = "مبلغ (ریال)"



@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'branch_name', 'account_number','format_to_thous_sep')
    ordering =['bank_name']

    def format_to_thous_sep(self, obj):
        return '{:,}'.format(round(obj.current_balance,0))
    format_to_thous_sep.short_description = "موجودی (ریال)"
