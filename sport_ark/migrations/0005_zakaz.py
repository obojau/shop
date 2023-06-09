# Generated by Django 4.1.5 on 2023-04-16 10:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport_ark', '0004_pod_category_category_img_alter_product_pod_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Сколько продуктов')),
                ('time_zakaz', models.DateField(auto_now=True, verbose_name='Время заказа')),
                ('product_zakaz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_ark.product', verbose_name='Продукт')),
                ('zakazatel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Заказавший')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['time_zakaz'],
            },
        ),
    ]
