# Generated by Django 3.1.5 on 2021-01-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers_all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_correct', models.CharField(max_length=500)),
                ('answer_correct', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quesiton', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
            ],
        ),
    ]
