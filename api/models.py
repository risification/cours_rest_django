from django.db import models


# Create your models here.


class Meal(models.Model):
    portions = (
        ('0.7', '0.7'),
        ('1', '1')
    )
    name = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    description = models.CharField(max_length=200, verbose_name='состав')
    price = models.PositiveIntegerField(max_length=50, verbose_name='цена')
    portion = models.CharField(choices=portions, max_length=50, verbose_name='порции')
