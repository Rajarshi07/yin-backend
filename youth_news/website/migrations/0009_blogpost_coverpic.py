# Generated by Django 3.1.2 on 2020-11-06 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_blogpost_istranding'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='coverPic',
            field=models.ImageField(default='/default_cover.png', upload_to='uploads/% Y/% m/% d/'),
        ),
    ]