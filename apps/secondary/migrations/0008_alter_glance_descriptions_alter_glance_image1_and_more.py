# Generated by Django 5.0.1 on 2024-01-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0007_rename_image_glance_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glance',
            name='descriptions',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография сверху'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография сверху'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография сверху'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография сверху'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография сверху'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='title1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='title2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='title3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='title4',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='glance',
            name='title5',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
    ]
