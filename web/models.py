from django.db import models
from django import utils

BANKS=[
    (1,"انصار"),
    (2,"سامان"),
    (3,"تجارت"),
    (4,"مسکن"),
    (5,"ملت"),
]
class BankAccount(models.Model):
    bank_name = models.IntegerField(u"نام بانک", choices=BANKS)
    account_number = models.CharField(u"شماره حساب", max_length=50, )
    sheba_number = models.CharField(u"شماره شبا", max_length=26, default='IR', null=True, blank=True)
    branch_name = models.CharField(u"نام شعبه", max_length=50, )
    initial_balance = models.DecimalField(u"موجودی اولیه ", max_digits=20, decimal_places = 2, default=0)
    current_balance = models.DecimalField(u"موجودی", max_digits=20, decimal_places=2, default=0)
    desc = models.CharField(u"توضیحات", max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "شماره حساب"
        verbose_name_plural = "شماره حسابهای بانکی"

    def __str__(self):
        return ("%s" % (self.account_number))


class ExpensCategory(models.Model):
    title = models.CharField(u"عنوان هزینه", max_length=100,)
    desc = models.CharField(u"توضیحات" ,max_length=200, null=True, blank=True)

    class Meta:
        order_with_respect_to = 'title'
        verbose_name = "عنوان هزینه"
        verbose_name_plural = "عناوین هزینه ها"

    def __str__(self):
        return self.title


class Expens(models.Model):
    category = models.ForeignKey(ExpensCategory, verbose_name="گروه هزینه", on_delete=models.CASCADE)
    from_bank_account = models.ForeignKey(BankAccount, verbose_name="برداشت از حساب", on_delete=models.CASCADE)
    desc = models.CharField("شرح هزینه", max_length=200)
    amount = models.DecimalField("مبلغ", max_digits=20, decimal_places=2)
    date = models.DateField("تاریخ", default=utils.timezone.now)
    
    class Meta:
        order_with_respect_to = 'date'
        verbose_name = "هزینه"
        verbose_name_plural = "هزینه ها"

    def save(self, *args, **kwargs):
        bank_account = BankAccount.objects.get(pk=self.from_bank_account.id)
        bank_account.current_balance -= self.amount
        bank_account.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.desc


class IncomeCategory(models.Model):
    title = models.CharField(u"عنوان درآمد", max_length=100,)
    desc = models.CharField(u"توضیحات" ,max_length=200, null=True, blank=True)

    class Meta:
        order_with_respect_to = 'title'
        verbose_name = "عنوان درآمد"
        verbose_name_plural = "عناوین درآمدها"

    def __str__(self):
        return self.title


class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, verbose_name = "گروه درآمد", on_delete=models.CASCADE,)
    to_bank_account = models.ForeignKey(BankAccount, verbose_name="واریز به حساب", on_delete=models.CASCADE)
    desc = models.CharField("شرح درآمد", max_length=200)
    amount = models.DecimalField("مبلغ درآمد", max_digits=20, decimal_places=2)
    date = models.DateField("تاریخ", default=utils.timezone.now)
    
    class Meta:
        order_with_respect_to = 'date'
        verbose_name = "درآمد"
        verbose_name_plural = "درآمد ها"

    def __str__(self):
        return self.desc

