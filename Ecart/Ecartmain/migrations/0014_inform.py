# Generated by Django 3.0.3 on 2020-04-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecartmain', '0013_delete_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='INFORM',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('Email', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField()),
                ('Eid', models.TextField(max_length=20)),
                ('Query', models.CharField(max_length=1000)),
            ],
        ),
    ]
