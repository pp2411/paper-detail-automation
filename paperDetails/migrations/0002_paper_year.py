# Generated by Django 3.2.3 on 2021-06-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperDetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
