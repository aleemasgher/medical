# Generated by Django 2.1 on 2018-08-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.CharField(max_length=250),
        ),
    ]
