# Generated by Django 4.0.2 on 2022-02-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_contact_userdatabase_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Contact', models.IntegerField()),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
