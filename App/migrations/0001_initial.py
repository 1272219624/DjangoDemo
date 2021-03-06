# Generated by Django 3.0.4 on 2020-03-14 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=255)),
                ('auth', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('pid', models.IntegerField()),
            ],
            options={
                'db_table': 'pro_city_area',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cou_id', models.IntegerField(default=1000)),
                ('cou_name', models.CharField(max_length=255)),
                ('cou_method', models.IntegerField(default=1)),
                ('cou_num', models.CharField(max_length=32)),
                ('is_open', models.BooleanField(default=True)),
                ('which_user', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_id', models.IntegerField(default=1000)),
                ('f_img', models.CharField(max_length=255)),
                ('f_name', models.CharField(max_length=128)),
                ('f_longname', models.CharField(max_length=255)),
                ('f_num', models.IntegerField(default=100)),
                ('scale', models.CharField(max_length=64)),
                ('price', models.FloatField(default=1)),
                ('eprice', models.FloatField(default=2)),
                ('type2id', models.IntegerField(default=1000)),
                ('type2name', models.CharField(max_length=128)),
                ('is_sell', models.BooleanField(default=True)),
                ('is_points', models.BooleanField(default=True)),
                ('is_hot', models.BooleanField(default=False)),
                ('place', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField(default=1000, unique=True)),
                ('typenames', models.CharField(max_length=32)),
                ('type2names', models.CharField(max_length=255)),
                ('is_hot', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='IndexSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_price', models.FloatField(default=0)),
                ('o_time', models.DateTimeField(auto_now=True)),
                ('o_status', models.IntegerField(default=1)),
                ('o_note', models.CharField(max_length=255)),
                ('o_addr', models.IntegerField(default=0)),
                ('o_points', models.IntegerField(default=0)),
                ('o_coupon', models.IntegerField(default=0)),
                ('o_vip', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=32, unique=True)),
                ('u_password', models.CharField(max_length=256)),
                ('u_email', models.CharField(max_length=64, unique=True)),
                ('u_phone', models.CharField(max_length=64)),
                ('u_icon', models.ImageField(upload_to='icons/%Y/%m/%d/')),
                ('all_points', models.IntegerField(default=0)),
                ('the_points', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
                ('addr_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cou_status', models.IntegerField(default=0)),
                ('cou_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Coupon')),
                ('cou_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_num', models.IntegerField(default=1)),
                ('is_add', models.BooleanField(default=True)),
                ('p_date', models.DateTimeField(auto_now=True)),
                ('p_price', models.FloatField(default=100)),
                ('p_detail', models.CharField(max_length=255)),
                ('p_status', models.BooleanField(default=False)),
                ('p_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderFoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_foods_num', models.IntegerField(default=1)),
                ('o_foods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Foods')),
                ('o_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='o_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_foods_num', models.IntegerField(default=1)),
                ('is_select', models.BooleanField(default=True)),
                ('c_addr', models.IntegerField(default=0)),
                ('c_foods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Foods')),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User')),
            ],
        ),
        migrations.CreateModel(
            name='Addr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_order_id', models.IntegerField(default=0)),
                ('a_city_id', models.IntegerField(default=0)),
                ('a_detail', models.CharField(max_length=125)),
                ('a_user_name', models.CharField(max_length=125)),
                ('a_tell', models.IntegerField()),
                ('a_time', models.IntegerField(default=1)),
                ('a_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User')),
            ],
        ),
    ]
