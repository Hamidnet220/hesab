from django.db import models

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
    desc = models.CharField("شرح هزینه", max_length=200)
    amount = models.DecimalField("مبلغ", max_digits=20, decimal_places=2)
    date = models.DateField("تاریخ")
    
    class Meta:
        order_with_respect_to = 'date'
        verbose_name = "هزینه"
        verbose_name_plural = "هزینه ها"

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
    desc = models.CharField("شرح درآمد", max_length=200)
    amount = models.DecimalField("مبلغ درآمد", max_digits=20, decimal_places=2)
    date = models.DateField("تاریخ")
    
    class Meta:
        order_with_respect_to = 'date'
        verbose_name = "درآمد"
        verbose_name_plural = "درآمد ها"

    def __str__(self):
        return self.desc

