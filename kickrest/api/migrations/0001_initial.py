# Generated by Django 2.1.4 on 2018-12-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backers_count', models.FloatField()),
                ('blurb', models.TextField()),
                ('catergory', models.TextField()),
                ('converted', models.FloatField()),
                ('country', models.CharField(max_length=10)),
                ('created_at', models.IntegerField()),
                ('creator', models.TextField()),
                ('currency', models.TextField()),
                ('deadline', models.IntegerField()),
                ('disable_communication', models.CharField(max_length=10)),
                ('fx_rate', models.FloatField()),
                ('goal', models.FloatField()),
                ('k_id', models.IntegerField()),
                ('launched_at', models.IntegerField()),
                ('location', models.TextField()),
                ('name', models.TextField()),
                ('photo', models.TextField()),
                ('pledged', models.FloatField()),
                ('profile', models.TextField()),
                ('slug', models.TextField()),
                ('source_url', models.TextField()),
                ('spotlight', models.CharField(max_length=10)),
                ('staff_pick', models.CharField(max_length=10)),
                ('state', models.TextField()),
                ('state_changed_at', models.IntegerField()),
                ('static_usd_rate', models.FloatField()),
                ('urls', models.TextField()),
                ('usd_pledged', models.FloatField()),
                ('usd_type', models.TextField()),
            ],
        ),
    ]