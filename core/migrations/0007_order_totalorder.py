# Generated by Django 2.2.14 on 2022-11-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20221120_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalOrder',
            field=models.FloatField(null=True),
        ),
    ]
