# Generated by Django 3.0.4 on 2020-03-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20200321_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_icon',
            field=models.ImageField(upload_to='icons/%Y/%m/%d/'),
        ),
    ]
