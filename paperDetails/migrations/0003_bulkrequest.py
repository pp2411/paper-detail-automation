# Generated by Django 3.2.3 on 2021-05-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperDetails', '0002_auto_20210529_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req', models.FileField(upload_to='Bulkrequests/')),
            ],
        ),
    ]