# Generated by Django 3.1.7 on 2021-03-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at'], 'verbose_name': 'Задача(y)', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterField(
            model_name='task',
            name='photo',
            field=models.ImageField(blank=True, default='static/img/caralog12.jpg', upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
