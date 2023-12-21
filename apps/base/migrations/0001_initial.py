# Generated by Django 5.0 on 2023-12-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок сайта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='слайд')),
            ],
            options={
                'verbose_name': 'Основные настройки сайта',
                'verbose_name_plural': 'Основные настройки сайта',
            },
        ),
    ]