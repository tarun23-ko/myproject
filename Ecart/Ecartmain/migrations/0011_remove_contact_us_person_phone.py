# Generated by Django 3.0.3 on 2020-04-16 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecartmain', '0010_contact_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_us',
            name='person_phone',
        ),
    ]