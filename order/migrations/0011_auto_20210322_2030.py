# Generated by Django 3.1.7 on 2021-03-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_order_promocode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]