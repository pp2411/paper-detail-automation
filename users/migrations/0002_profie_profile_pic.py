# Generated by Django 3.2.3 on 2021-05-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profie',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
