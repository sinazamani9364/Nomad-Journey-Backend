# Generated by Django 4.1.7 on 2023-06-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_coin_to_buy_alter_user_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='new_password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='old_password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
