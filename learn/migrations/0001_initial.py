# Generated by Django 3.1.5 on 2021-01-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=1000)),
                ('ans1', models.CharField(max_length=100)),
                ('ans2', models.CharField(max_length=100)),
                ('ans3', models.CharField(max_length=100)),
                ('ans4', models.CharField(max_length=100)),
            ],
        ),
    ]
