# Generated by Django 3.1.3 on 2020-11-27 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_expens_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='category',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='web.incomecategory', verbose_name='گروه درآمد'),
            preserve_default=False,
        ),
    ]
