# Generated by Django 3.0.3 on 2020-04-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecartmain', '0019_information_phone4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='phone4',
            field=models.IntegerField(null=True),
        ),
    ]