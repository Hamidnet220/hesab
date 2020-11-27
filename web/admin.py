from django.contrib import admin
from .models import Expens, Income, IncomeCategory, ExpensCategory

admin.site.register(Expens)
admin.site.register(Income)
admin.site.register(ExpensCategory)
admin.site.register(IncomeCategory)

