# Generated by Django 3.0.3 on 2020-04-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecartmain', '0030_auto_20200425_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=0, max_length=60),
        ),
    ]
