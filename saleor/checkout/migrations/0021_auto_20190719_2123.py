# Generated by Django 2.2.3 on 2019-07-19 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0020_checkoutshipping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutshipping',
            old_name='order',
            new_name='checkout',
        ),
    ]