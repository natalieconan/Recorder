# Generated by Django 4.2.7 on 2023-11-29 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
