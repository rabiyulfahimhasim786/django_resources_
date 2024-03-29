# Generated by Django 4.1 on 2022-09-21 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Adhar',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.person')),
                ('signature', models.TextField()),
                ('adhar_no', models.TextField(max_length=100)),
            ],
        ),
    ]
