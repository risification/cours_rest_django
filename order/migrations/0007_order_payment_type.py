# Generated by Django 3.1.7 on 2021-03-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('card', 'card'), ('cash', 'cash')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]
