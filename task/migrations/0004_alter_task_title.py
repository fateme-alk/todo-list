# Generated by Django 4.2.7 on 2024-01-29 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_remove_task_doer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
