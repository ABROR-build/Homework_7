# Generated by Django 5.0.6 on 2024-05-09 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='image',
            field=models.ImageField(blank=True, default='/default_images/car.png', null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='company',
            name='comp_logo',
            field=models.ImageField(blank=True, default='default_images/user.png', null=True, upload_to='company_logos/'),
        ),
    ]