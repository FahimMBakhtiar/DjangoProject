# Generated by Django 2.2.14 on 2022-04-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220416_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.CharField(choices=[('ADI', 'ADIDAS'), ('NIK', 'NIKE'), ('UAM', 'UNDER ARMOUR'), ('VAN', 'VANS')], max_length=3),
        ),
    ]
