# Generated by Django 3.2.3 on 2021-05-29 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_rename_profie_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('empId', models.CharField(max_length=20)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('authors', models.CharField(max_length=150)),
                ('publication', models.CharField(max_length=150)),
                ('noOfCitations', models.IntegerField()),
                ('citation_id', models.CharField(max_length=30)),
                ('citation_link', models.URLField()),
                ('year', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paperDetails.faculty')),
            ],
        ),
    ]