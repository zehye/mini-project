# Generated by Django 2.1.1 on 2018-09-30 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('photo_review', models.ImageField(blank=True, upload_to='')),
                ('text_review', models.TextField(blank=True)),
                ('photo_event', models.ImageField(blank=True, upload_to='')),
                ('text_event', models.TextField(blank=True)),
                ('address_latitude', models.DecimalField(blank=True, decimal_places=14, max_digits=16, verbose_name='Google MAP API 위도')),
                ('address_longitude', models.DecimalField(blank=True, decimal_places=14, max_digits=17, verbose_name='Google MAP API 경도')),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitionTotalList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=30)),
            ],
        ),
    ]