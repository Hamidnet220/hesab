# Generated by Django 3.1.3 on 2020-12-02 16:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20201128_0445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='نام')),
                ('last_name', models.CharField(max_length=60, verbose_name='نام')),
            ],
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='bank_name',
            field=models.IntegerField(choices=[(1, 'انصار'), (2, 'سامان'), (3, 'تجارت'), (4, 'مسکن'), (5, 'ملت'), (0, 'کیف پول')], verbose_name='نام بانک'),
        ),
        migrations.AlterField(
            model_name='expens',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ'),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.IntegerField(choices=[(1, 'واریز'), (2, 'برداشت'), (3, 'انتقال')], default=1, verbose_name='نوع تراکنش')),
                ('description', models.CharField(max_length=200, verbose_name='شرح تراکنش')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='مبلغ تراکنش')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ')),
                ('other_data', models.CharField(blank=True, max_length=200, null=True, verbose_name='سایر توضیحات')),
                ('bank_accout', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.bankaccount', verbose_name='شماره حساب')),
            ],
            options={
                'verbose_name': 'تراکنش',
                'verbose_name_plural': 'تراکنش ها',
                'order_with_respect_to': 'date',
            },
        ),
    ]