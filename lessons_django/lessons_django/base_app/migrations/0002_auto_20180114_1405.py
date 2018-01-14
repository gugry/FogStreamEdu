# Generated by Django 2.0.1 on 2018-01-14 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Книги',
                'verbose_name': 'Книга',
                'ordering': ('-name',),
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('-sername',), 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='patronymic',
            field=models.CharField(max_length=32, verbose_name='Отчество '),
        ),
        migrations.AlterField(
            model_name='author',
            name='sername',
            field=models.CharField(max_length=32, verbose_name='Фамилия'),
        ),
    ]
