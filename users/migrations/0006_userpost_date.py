# Generated by Django 3.0.7 on 2020-06-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200614_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
