# Generated by Django 4.1.7 on 2023-03-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0011_temp_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('architech_id', models.IntegerField(default=0)),
                ('payment', models.IntegerField(default=0)),
            ],
        ),
    ]