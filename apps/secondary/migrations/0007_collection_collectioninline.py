# Generated by Django 5.0.1 on 2024-01-02 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0006_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография сверху')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_info', to='secondary.glance')),
            ],
            options={
                'unique_together': {('place_info', 'image')},
            },
        ),
    ]
