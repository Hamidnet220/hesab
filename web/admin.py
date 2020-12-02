from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from jalali_date import date2jalali

from .models import BankAccount, Expens, Income, IncomeCategory, ExpensCategory, Transaction, TransCategory


admin.site.register(ExpensCategory)
admin.site.register(IncomeCategory)
admin.site.register(TransCategory)


def convert_date_to_jalali(obj):
    return date2jalali(obj.date)
convert_date_to_jalali.short_description = "تاریخ"

@admin.register(Transaction)
class TransactionAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['bank_account','description','amount','trans_category', convert_date_to_jalali,
    'transaction_type']
    list_filter=['bank_account','trans_category']

@admin.register(Expens)
class ExpensAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('category', 'desc', 'format_to_thous_sep', convert_date_to_jalali,)
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
    list_display = ('category', 'desc', 'format_to_thous_sep', convert_date_to_jalali,)
    list_filter = ('category',)
    ordering =['-date']
    actions = ['delete_income']
    search_field = ['desc']

    def format_to_thous_sep(self, obj):
        return '{:,}'.format(round(obj.amount,0))
    format_to_thous_sep.short_description = "مبلغ (ریال)"

    def save_model(self, request, obj, form, change):
        bank_account = obj.to_bank_account
        bank_account.current_balance += obj.amount
        bank_account.save()
        super().save_model(request, obj, form, change)

    def delete_income(self, request, queryset):
        for obj in queryset:
            bank_acc = obj.to_bank_account
            bank_acc.current_balance -= obj.amount
            bank_acc.save()
            obj.delete()
    delete_income.short_description = 'حذف درآمد'


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'branch_name', 'account_number','format_to_thous_sep')
    ordering =['bank_name']

    def format_to_thous_sep(self, obj):
        return '{:,}'.format(round(obj.current_balance,0))
    format_to_thous_sep.short_description = "موجودی (ریال)"

