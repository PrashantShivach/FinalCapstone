# Generated by Django 3.2.6 on 2021-08-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitorname', models.CharField(max_length=100)),
                ('mobileno', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=300)),
                ('apartment', models.CharField(max_length=100)),
                ('floor', models.CharField(max_length=50)),
                ('whomtomeet', models.CharField(max_length=100)),
                ('reasontomeet', models.CharField(max_length=200)),
                ('intime', models.CharField(max_length=50)),
                ('vdate', models.DateField()),
                ('remark', models.CharField(max_length=500)),
                ('outtime', models.CharField(max_length=50)),
            ],
        ),
    ]
