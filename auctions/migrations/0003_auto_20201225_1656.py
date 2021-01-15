# Generated by Django 3.0 on 2020-12-25 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_winner_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing'),
        ),
        migrations.AddField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing'),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing'),
        ),
    ]
