# Generated by Django 4.2.6 on 2023-10-11 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Chat closed time')),
                ('is_active', models.BooleanField(default=True, verbose_name='Status of chat')),
                ('chat_user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL)),
                ('chat_user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'chats',
                'ordering': ['started_time'],
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=140)),
                ('message_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('message_datetime', models.DateTimeField(auto_now_add=True)),
                ('message_status', models.BooleanField(default=True)),
                ('message_reaction', models.BooleanField(blank=True, null=True)),
                ('message_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_chat.chats')),
                ('message_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'chats_messages',
                'ordering': ['message_datetime'],
            },
        ),
    ]
