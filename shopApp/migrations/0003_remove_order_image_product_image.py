# Generated by Django 4.2.4 on 2023-10-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_order_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
