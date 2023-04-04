# Generated by Django 3.2.18 on 2023-04-04 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('futurehomeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='listing_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('ber_category', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'For Sale'), (1, 'Sold')], default=0)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='futurehomeapp.listing')),
            ],
        ),
    ]
