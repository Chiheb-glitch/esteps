# Generated by Django 4.1.7 on 2023-03-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_friend_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='created_at',
            field=models.CharField(max_length=8),
        ),
    ]
