# Generated by Django 2.2.14 on 2022-12-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20221202_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='ref_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
