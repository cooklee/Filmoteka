# Generated by Django 3.2.9 on 2021-12-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0004_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='filmy.Genre'),
        ),
    ]
