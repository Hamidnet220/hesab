from django.db import models
from django import utils

BANKS=[
    (1,"انصار"),
    (2,"سامان"),
    (3,"تجارت"),
    (4,"مسکن"),
    (5,"ملت"),
    (0,"کیف پول"),

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
        if self.bank_name == 0:
            return ("%s" % (self.get_bank_name_display())) # کیف پول
        else:
            return ("%s" % (self.account_number))

            
TRANS_CATEGROY_TYPE =[
    (1,"هزینه"),
    (2,"درآمد"),
    (3,"انتقال"),
]
class TransCategory(models.Model):
    title = models.CharField(u"عنوان گروه", max_length=100,)
    category_type = models.IntegerField("نوع گروه",choices=TRANS_CATEGROY_TYPE)
    desc = models.CharField(u"توضیحات" ,max_length=200, null=True, blank=True)

    class Meta:
        order_with_respect_to = 'title'
        verbose_name = "گروه تراکنش"
        verbose_name_plural = " گروه تراکنش ها"

    def __str__(self):
        return self.title


TRANSACTION_TYPE =[
    (1,"واریز"),
    (2,"برداشت"),
]
class Transaction(models.Model):
    transaction_type = models.IntegerField("نوع تراکنش", choices=TRANSACTION_TYPE, default=1)
    trans_category = models.ForeignKey(TransCategory,verbose_name=" گروه", on_delete=models.PROTECT,null=True,blank=True)
    bank_account = models.ForeignKey(BankAccount, verbose_name="شماره حساب", on_delete=models.PROTECT)
    description = models.CharField("شرح تراکنش",max_length=200)
    amount = models.DecimalField("مبلغ تراکنش", max_digits=20, decimal_places=2)
    date = models.DateTimeField("تاریخ", default=utils.timezone.now)
    other_data = models.CharField("سایر توضیحات",max_length=200, blank=True, null=True)

    class Meta:
        order_with_respect_to = 'date'
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش ها"

    def __str__(self):
        return self.description
    
