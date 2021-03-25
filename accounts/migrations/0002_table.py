# Generated by Django 3.1.7 on 2021-03-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('main', 'main'), ('vip', 'vip'), ('street', 'street')], max_length=50)),
                ('status', models.CharField(choices=[('reserved', 'reserved'), ('empty', 'empty')], max_length=50)),
            ],
        ),
    ]