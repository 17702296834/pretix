# Generated by Django 2.2.4 on 2019-11-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0140_voucher_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='sorting_rank',
            field=models.BigIntegerField(default=0),
        ),
    ]
