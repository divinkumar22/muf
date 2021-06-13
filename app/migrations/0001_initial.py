# Generated by Django 2.2.10 on 2021-06-11 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PickupMan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=250)),
                ('phone', models.CharField(default='', max_length=13)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('aadhaar_card', models.CharField(default='', max_length=12)),
                ('total_amount', models.FloatField(default=0)),
                ('address', models.TextField(default='')),
                ('area', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=250)),
                ('email_id', models.EmailField(default='', max_length=254, unique=True)),
                ('phone', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=250)),
                ('phone', models.CharField(default='', max_length=13)),
                ('username', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('aadhaar_card', models.CharField(default='', max_length=12)),
                ('pan_card', models.CharField(default='', max_length=20)),
                ('total_amount', models.FloatField(default=0)),
                ('address', models.TextField(default='')),
                ('area', models.CharField(default='', max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], default='', max_length=250)),
                ('transaction_amount', models.FloatField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pickup_man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PickupMan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(null=True)),
                ('otp_time', models.DateTimeField(null=True)),
                ('counter', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
    ]