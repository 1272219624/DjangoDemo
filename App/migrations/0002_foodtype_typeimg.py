# Generated by Django 3.0.4 on 2020-03-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtype',
            name='typeimg',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
