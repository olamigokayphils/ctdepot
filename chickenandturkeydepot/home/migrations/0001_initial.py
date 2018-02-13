# Generated by Django 2.0.2 on 2018-02-10 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('full_name', models.CharField(blank=True, max_length=400, null=True, verbose_name='full name')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', home.models.UserAccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meat_type', models.CharField(blank=True, choices=[('c', 'chiken meat'), ('t', 'turkey meat')], default='', help_text='Select meat type', max_length=1)),
                ('cut_type', models.CharField(blank=True, choices=[('Whole', 'WOG[Whole]'), ('Tenderloin', 'Tenderloin'), ('Thigh', 'Thigh'), ('Drumstick', 'Drumstick'), ('Whole Wing', 'Whole Wing'), ('Breast Fillet', 'Breast Fillet'), ('Tenders', 'Tenders'), ('Legs', 'Legs')], default='', help_text='Select cut type', max_length=50)),
                ('Weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Order', primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Order confirmed', max_length=30)),
                ('meat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Meat')),
            ],
            options={
                'ordering': ['date_time'],
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]