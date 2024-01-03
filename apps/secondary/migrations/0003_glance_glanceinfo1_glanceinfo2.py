# Generated by Django 5.0.1 on 2024-01-02 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0002_alter_style_options_styleinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='GlanceInfo1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография сверху')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glance_info1', to='secondary.glance')),
            ],
            options={
                'unique_together': {('place_info', 'image')},
            },
        ),
        migrations.CreateModel(
            name='GlanceInfo2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография снизу')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glance_info2', to='secondary.glance')),
            ],
            options={
                'unique_together': {('place_info', 'image')},
            },
        ),
    ]
