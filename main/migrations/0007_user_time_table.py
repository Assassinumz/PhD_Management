# Generated by Django 4.1.7 on 2023-04-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_profile_picture_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time_table',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
