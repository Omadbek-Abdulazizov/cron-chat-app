# Generated by Django 4.2.7 on 2024-02-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_habarlar_remove_hodimlar_vaqt'),
    ]

    operations = [
        migrations.AddField(
            model_name='habarlar',
            name='hodim',
            field=models.ManyToManyField(to='main_app.hodimlar'),
        ),
    ]
