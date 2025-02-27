# Generated by Django 2.2.3 on 2019-07-19 15:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_checkout_gift_cards'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutShipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('time_slot', models.CharField(max_length=64, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='checkout.Checkout')),
            ],
        ),
    ]
