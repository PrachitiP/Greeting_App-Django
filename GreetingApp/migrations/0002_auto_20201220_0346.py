# Generated by Django 3.0.5 on 2020-12-19 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreetingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greetingcard',
            name='message',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='greetingcard',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
