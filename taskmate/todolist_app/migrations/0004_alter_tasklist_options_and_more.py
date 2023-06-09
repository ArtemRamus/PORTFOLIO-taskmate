# Generated by Django 4.2 on 2023-05-21 16:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist_app', '0003_alter_tasklist_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'ordering': ['id']},
        ),
        migrations.AlterUniqueTogether(
            name='tasklist',
            unique_together={('task', 'owner')},
        ),
    ]
