# Generated by Django 4.2.5 on 2023-09-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelslip',
            name='status',
            field=models.IntegerField(),
        ),
    ]
