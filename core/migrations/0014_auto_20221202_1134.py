# Generated by Django 2.2.14 on 2022-12-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20221201_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('FU', 'Furniture'), ('VE', 'Vehicles'), ('CL', 'Clothes'), ('OD', 'Outdoor'), ('BP', 'Backpacks')], max_length=2),
        ),
    ]
