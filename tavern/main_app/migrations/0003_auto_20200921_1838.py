# Generated by Django 3.1.1 on 2020-09-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200920_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='date of next session'),
        ),
    ]
