# Generated by Django 4.1.7 on 2023-04-22 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_interests_alter_user_langf_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='User_nationality',
            new_name='s',
        ),
    ]
