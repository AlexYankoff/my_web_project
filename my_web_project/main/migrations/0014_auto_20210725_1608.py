# Generated by Django 3.2.5 on 2021-07-25 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_remove_homework_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='id',
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user'),
            preserve_default=False,
        ),
    ]
