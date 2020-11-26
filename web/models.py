from django.db import models

class Expens(models.Model):
    desc = models.CharField("شرح هزینه", max_length=200)
    amount = models.DecimalField("مبلغ", max_digits=20, decimal_places=2)
    date = models.DateField("تاریخ")


    def __str__(self):
        return self.desc


class Income(models.Model):
    desc = models.CharField("شرح درآمد", max_length=200)
    amount = models.DecimalField("مبلغ درآمد", max_digits=20, decimal_places=2)
    date = models.DateField("تاریخ")
    
    class Meta:
        order_with_respect_to = 'date'
        
    def __str__(self):
        return self.desc