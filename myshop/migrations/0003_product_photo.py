# Generated by Django 5.0.6 on 2024-05-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_alter_client_client_reg_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photos/'),
        ),
    ]