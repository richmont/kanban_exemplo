# Generated by Django 4.2.3 on 2023-07-07 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_back', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='titulo',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
