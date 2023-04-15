# Generated by Django 4.1.7 on 2023-04-15 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('announcement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AncRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('req_anc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='announcement.announcement')),
            ],
        ),
    ]
