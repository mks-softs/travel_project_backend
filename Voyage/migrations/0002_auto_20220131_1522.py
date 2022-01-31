# Generated by Django 3.1.12 on 2022-01-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voyage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='is_super',
            new_name='is_superuser',
        ),
        migrations.AddField(
            model_name='myuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='register_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
