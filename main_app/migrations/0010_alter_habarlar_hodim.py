# Generated by Django 4.2.7 on 2024-02-28 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_habarlar_vaqt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habarlar',
            name='hodim',
            field=models.ManyToManyField(blank=True, to='main_app.hodimlar'),
        ),
    ]
