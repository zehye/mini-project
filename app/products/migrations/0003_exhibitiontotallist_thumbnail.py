# Generated by Django 2.1.1 on 2018-09-30 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180930_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitiontotallist',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='exhibition_list'),
        ),
    ]