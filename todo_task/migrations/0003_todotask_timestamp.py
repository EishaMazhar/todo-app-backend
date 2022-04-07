# Generated by Django 4.0.3 on 2022-04-07 05:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_task', '0002_todotask_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotask',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]