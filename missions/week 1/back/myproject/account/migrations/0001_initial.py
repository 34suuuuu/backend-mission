# Generated by Django 4.0.1 on 2022-01-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
