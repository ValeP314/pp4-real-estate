# Generated by Django 3.2.18 on 2023-04-24 22:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('futurehomeapp', '0016_auto_20230422_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM')], default='3 PM', max_length=10)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
