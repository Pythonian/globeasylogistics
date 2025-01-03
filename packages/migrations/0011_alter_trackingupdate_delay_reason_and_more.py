# Generated by Django 5.1.4 on 2025-01-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0010_remove_trackingupdate_delivery_proof_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingupdate',
            name='delay_reason',
            field=models.CharField(blank=True, choices=[('weather', 'Weather Delay'), ('customs', 'Customs Hold'), ('traffic', 'Traffic Congestion'), ('mechanical', 'Mechanical Issue')], help_text='Reason for delay, if applicable.', max_length=20, null=True, verbose_name='Delay Reason'),
        ),
        migrations.AlterField(
            model_name='trackingupdate',
            name='status',
            field=models.CharField(choices=[('awaiting_pickup', 'Awaiting Pickup'), ('in_transit', 'In Transit'), ('delivered', 'Delivered'), ('returned', 'Returned'), ('delayed', 'Delayed')], help_text='The current status of the package.', max_length=20, verbose_name='Status'),
        ),
    ]
