# Generated by Django 4.1.7 on 2023-04-04 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_user_json'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='json',
            new_name='publications',
        ),
    ]
