# Generated by Django 4.0.5 on 2022-06-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangowedapp1', '0003_remove_venue_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]