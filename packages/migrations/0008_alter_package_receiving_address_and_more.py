# Generated by Django 5.1.4 on 2024-12-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_remove_package_customer_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='receiving_address',
            field=models.CharField(help_text='The destination address for the package.', max_length=255, verbose_name='Receiving Address'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='address',
            field=models.CharField(help_text='The physical address of the recipient.', max_length=255, verbose_name='Recipient Address'),
        ),
        migrations.AlterField(
            model_name='sender',
            name='address',
            field=models.CharField(help_text='The physical address of the sender.', max_length=255, verbose_name='Sender Address'),
        ),
    ]