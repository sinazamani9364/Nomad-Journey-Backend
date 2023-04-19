# Generated by Django 4.1.7 on 2023-04-19 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateField(blank=True, null=True)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('anc_status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('D', 'Done'), ('E', 'Expired')], default='P', max_length=1)),
                ('arrival_date_is_flexible', models.BooleanField(blank=True, default=False, null=True)),
                ('departure_date_is_flexible', models.BooleanField(blank=True, default=False, null=True)),
                ('anc_description', models.TextField(blank=True, max_length=500, null=True)),
                ('anc_timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('travelers_count', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15')], null=True)),
                ('anc_city', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='utils.city')),
                ('announcer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='announcer_anc', to=settings.AUTH_USER_MODEL)),
                ('main_host', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='main_host_anc', to=settings.AUTH_USER_MODEL)),
                ('volunteer_hosts', models.ManyToManyField(blank=True, related_name='hosts_anc', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
