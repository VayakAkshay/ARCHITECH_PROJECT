# Generated by Django 4.1.7 on 2023-03-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_id', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=100)),
                ('acc_type', models.TextField(default='', max_length=100)),
            ],
        ),
    ]
