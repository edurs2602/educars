# Generated by Django 5.0.7 on 2024-07-14 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user_email',
        ),
    ]
