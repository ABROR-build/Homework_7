# Generated by Django 5.0.6 on 2024-05-12 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_cars_image_alter_company_comp_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='date_uploaded',
        ),
    ]