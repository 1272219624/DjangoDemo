# Generated by Django 3.0.4 on 2020-04-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0020_points_is_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='InSign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
