from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from jalali_date import date2jalali

from .models import BankAccount, Transaction, TransCategory


admin.site.register(TransCategory)


def convert_date_to_jalali(obj):
    return date2jalali(obj.date)
convert_date_to_jalali.short_description = "تاریخ"

@admin.register(Transaction)
class TransactionAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['bank_account','description','format_to_thous_sep','trans_category', convert_date_to_jalali,
    'transaction_type']
    ordering = ['-date'] 
    list_filter=['bank_account','trans_category']

    actions = ['delete_trans']

    def format_to_thous_sep(self, obj):
        return '{:,}'.format(round(obj.amount,0))
    format_to_thous_sep.short_description = "مبلغ (ریال)"


    def delete_trans(self, request, queryset):
        for obj in queryset:
            bank_acc = obj.bank_account
            if obj.transaction_type == 1:
                bank_acc.current_balance -= obj.amount
            elif obj.transaction_type == 2:
                 bank_acc.current_balance += obj.amount
            bank_acc.save()
            obj.delete()
    delete_trans.short_description = "حذف تراکنش"


    def save_model(self, request, obj, form, change):
        bank_account = obj.to_bank_account
        if obj.transaction_type == 1:
            bank_acc.current_balance += obj.amount
        elif obj.transaction_type == 2:
            bank_acc.current_balance -= obj.amount

        bank_account.save()
        super().save_model(request, obj, form, change)


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'branch_name', 'account_number','format_to_thous_sep')
    ordering =['bank_name']

    def format_to_thous_sep(self, obj):
        return '{:,}'.format(round(obj.current_balance,0))
    format_to_thous_sep.short_description = "موجودی (ریال)"

