# Generated by Django 2.1.7 on 2020-06-10 16:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0019_auto_20200514_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
              
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
    ]
