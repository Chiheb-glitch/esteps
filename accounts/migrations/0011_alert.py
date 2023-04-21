# Generated by Django 4.1.3 on 2023-04-20 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_group_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_date', models.CharField(max_length=500)),
                ('alert_bio', models.CharField(max_length=500)),
                ('alert_latitude', models.FloatField()),
                ('alert_longitude', models.FloatField()),
                ('alert_receiver', models.ManyToManyField(related_name='received_alerts', to='accounts.profile')),
                ('alert_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
