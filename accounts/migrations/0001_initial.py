# Generated by Django 3.1.7 on 2021-03-17 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(default=0)),
                ('date_start', models.DateField(auto_now_add=True)),
                ('date_end', models.DateField()),
                ('salary', models.PositiveIntegerField(default=0)),
                ('schedule', models.CharField(choices=[('2/2', '2/2'), ('5/2', '5/2')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
