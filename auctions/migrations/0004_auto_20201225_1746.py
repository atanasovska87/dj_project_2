# Generated by Django 3.0 on 2020-12-25 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201225_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='category',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('listing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing')),
                ('parents', models.ForeignKey(blank=True, default=1, limit_choices_to={'parents__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Category')),
            ],
        ),
    ]
