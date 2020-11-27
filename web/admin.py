from django.contrib import admin
from .models import BankAccount, Expens, Income, IncomeCategory, ExpensCategory

admin.site.register(ExpensCategory)
admin.site.register(IncomeCategory)




@admin.register(Expens)
class ExpensAdmin(admin.ModelAdmin):
    list_display = ('category', 'desc', 'format_to_thous_sep', 'date',)
    list_filter = ('category',)
    ordering = ['-date'] 
    actions = ['delete_expens']

    def format_to_thous_sep(self, obj):
        return '{:,}'.format(round(obj.amount,0))
    format_to_thous_sep.short_description = "مبلغ (ریال)"

    def delete_expens(self, request, queryset):
        for obj in queryset:
            bank_acc = obj.from_bank_account
            bank_acc.current_balance += obj.amount
            bank_acc.save()
            obj.delete()
    delete_expens.short_description = "حذف هزینه"


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
