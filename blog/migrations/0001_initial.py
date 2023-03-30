# Generated by Django 4.1.7 on 2023-03-30 11:22

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blog_title', models.CharField(blank=True, max_length=500)),
                ('blog_text', models.TextField(blank=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='blogs_image')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='blog_title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='TaggedModel', to='blog.tag')),
            ],
        ),
    ]
