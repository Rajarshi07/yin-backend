# Generated by Django 3.1.2 on 2020-11-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_advertisement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='reactangleImage',
            field=models.ImageField(default='/ads_image/rectangle_ads_default.png', upload_to='ads_image/'),
        ),
    ]
