# Generated by Django 3.1.2 on 2020-11-19 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20201119_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='reactangleImage',
            new_name='rectangleImage',
        ),
    ]
