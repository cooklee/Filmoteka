# Generated by Django 3.2.9 on 2021-12-04 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0003_film_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
