# Generated by Django 3.1.7 on 2021-03-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210319_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('default', 'default'), ('non active', 'non active')], default='non active', max_length=15),
        ),
    ]