# Generated by Django 3.1.7 on 2021-03-23 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0005_auto_20210323_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
    ]
