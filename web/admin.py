from django.contrib import admin
from .models import Expens, Income, IncomeCategory, ExpensCategory

admin.site.register(ExpensCategory)
admin.site.register(IncomeCategory)


def format_amount_to_thous_sep(obj):
    return '{:,}'.format(round(obj.amount,0))
format_amount_to_thous_sep.short_description = "مبلغ (ریال)"


@admin.register(Expens)
class ExpensAdmin(admin.ModelAdmin):
    list_display = ('category', 'desc', format_amount_to_thous_sep, 'date',)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('category', 'desc', format_amount_to_thous_sep, 'date',)
