# Generated by Django 5.2 on 2025-07-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.CharField(blank=True, null=True, verbose_name='Id места'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]
