# Generated by Django 5.1.2 on 2024-10-18 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='tagline',
            field=models.CharField(max_length=50),
        ),
    ]