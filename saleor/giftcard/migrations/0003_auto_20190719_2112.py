# Generated by Django 2.2.3 on 2019-07-19 15:42

from django.db import migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0002_auto_20190717_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcard',
            name='current_balance',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='giftcard',
            name='initial_balance',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, max_digits=12),
        ),
    ]
