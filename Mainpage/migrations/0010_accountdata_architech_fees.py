# Generated by Django 4.1.7 on 2023-03-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0009_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdata',
            name='architech_fees',
            field=models.IntegerField(default=0),
        ),
    ]
