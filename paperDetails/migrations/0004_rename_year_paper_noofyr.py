# Generated by Django 3.2.3 on 2021-06-01 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paperDetails', '0003_bulkrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='year',
            new_name='noOfYr',
        ),
    ]
