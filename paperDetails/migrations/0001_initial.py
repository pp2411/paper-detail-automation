# Generated by Django 3.2.3 on 2021-06-01 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_rename_profie_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req', models.FileField(upload_to='Bulkrequests/')),
            ],
        ),
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
                ('link', models.URLField(null=True)),
                ('authors', models.CharField(max_length=150, null=True)),
                ('publication', models.CharField(max_length=150, null=True)),
                ('noOfCitations', models.IntegerField(null=True)),
                ('citation_id', models.CharField(max_length=30, null=True)),
                ('citation_link', models.URLField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paperDetails.faculty')),
            ],
        ),
    ]
