# Generated by Django 3.2.5 on 2021-07-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_homework_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='title',
            field=models.CharField(default='no', max_length=30),
            preserve_default=False,
        ),
    ]
