# Generated by Django 4.1.7 on 2023-05-23 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='ans_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ans', to='announcement.announcement'),
            preserve_default=False,
        ),
    ]
