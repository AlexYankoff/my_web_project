# Generated by Django 3.2.5 on 2021-07-20 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210720_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='id',
            new_name='user',
        ),
    ]