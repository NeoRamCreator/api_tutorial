# Generated by Django 4.0.1 on 2022-01-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.CharField(default='default-a1', max_length=255)),
                ('a2', models.CharField(default='default-a2', max_length=255)),
                ('a3', models.CharField(default='default-a3', max_length=255)),
                ('a4', models.CharField(default='default-a4', max_length=255)),
            ],
        ),
    ]
