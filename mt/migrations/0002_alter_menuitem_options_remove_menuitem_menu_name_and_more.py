# Generated by Django 5.0.4 on 2024-04-15 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu_name',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='named_url',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='order',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
