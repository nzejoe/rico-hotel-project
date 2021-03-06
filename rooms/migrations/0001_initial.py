# Generated by Django 3.2.8 on 2021-10-24 10:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='rooms')),
                ('room_number', models.CharField(max_length=20)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('person_capacity', models.IntegerField()),
                ('floor', models.CharField(choices=[('', 'Choose'), ('ground floor', 'Ground Floor'), ('first floor', 'First Floor')], default='Choose', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_available', models.BooleanField(default=True)),
                ('room_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.roomtype')),
            ],
        ),
    ]
