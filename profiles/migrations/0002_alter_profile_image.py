# Generated by Django 3.2.21 on 2023-10-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_cgysu0', upload_to='images/'),
        ),
    ]
