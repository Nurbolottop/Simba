# Generated by Django 5.0.1 on 2024-01-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_alter_glance_options_glanceinfo_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_goods', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('now_price', models.CharField(max_length=255, verbose_name='Цена сейчас')),
                ('before_price', models.CharField(max_length=255, verbose_name='Цена раньше')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
    ]
