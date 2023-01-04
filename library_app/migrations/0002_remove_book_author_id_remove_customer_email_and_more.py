# Generated by Django 4.1.5 on 2023-01-03 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Billy Lee', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='in_stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='published_at',
            field=models.DateTimeField(default=datetime.date(2015, 12, 17)),
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='00640 James Plain\nMichaelville, MD 51245', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='Sonya Bridges', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='David Collins', max_length=50),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
