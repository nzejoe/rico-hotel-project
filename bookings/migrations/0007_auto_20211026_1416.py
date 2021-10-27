# Generated by Django 3.2.8 on 2021-10-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_bookedroom_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedroom',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookedroom',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]