# Generated by Django 5.0.4 on 2024-04-15 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('named_url', models.CharField(blank=True, max_length=255)),
                ('menu_name', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='mt.menuitem')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
