# Generated by Django 3.1.12 on 2022-01-24 12:56

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=300)),
                ('numero_compagnie', models.CharField(max_length=15)),
                ('data', djongo.models.fields.JSONField(default={'key': 'value'})),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('password', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_client', models.BooleanField(default=True)),
                ('is_moniteur', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
