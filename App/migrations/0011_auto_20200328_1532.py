# Generated by Django 3.0.4 on 2020-03-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_user_all_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='c_foods',
        ),
        migrations.AddField(
            model_name='cart',
            name='c_foods_id',
            field=models.IntegerField(default=1000),
        ),
    ]
