# Generated by Django 3.2.9 on 2021-12-05 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0005_film_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='screenplay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writen', to='filmy.person'),
        ),
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directed_by', to='filmy.person'),
        ),
    ]