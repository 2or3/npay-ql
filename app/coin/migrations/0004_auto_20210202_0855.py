# Generated by Django 3.1.6 on 2021-02-02 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0003_auto_20210202_0609'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoinTransactions',
            new_name='Transactions',
        ),
    ]
