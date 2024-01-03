# Generated by Django 5.0.1 on 2024-01-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description1',
            field=models.CharField(default=1, max_length=255, verbose_name='Мини описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='description2',
            field=models.CharField(default=1, max_length=255, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.CharField(default=1, max_length=25, verbose_name='Заголовок'),
            preserve_default=False,
        ),
    ]