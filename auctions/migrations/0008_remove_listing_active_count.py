# Generated by Django 3.0 on 2021-01-11 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_listing_active_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='active_count',
        ),
    ]