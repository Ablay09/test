# Generated by Django 2.1.1 on 2018-09-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180930_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateField(verbose_name='Created date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='finished_date',
            field=models.DateField(verbose_name='Finished date'),
        ),
        migrations.AlterField(
            model_name='task_list',
            name='time',
            field=models.DateField(verbose_name='Created time of list is'),
        ),
    ]
