# Generated by Django 3.1.5 on 2021-01-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq_test', '0005_delete_answers_alll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
            ],
        ),
    ]
