# Generated by Django 3.1.3 on 2020-12-02 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20201202_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ'),
        ),
    ]
