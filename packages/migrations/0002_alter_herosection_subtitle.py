# Generated by Django 5.1.4 on 2024-12-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herosection',
            name='subtitle',
            field=models.CharField(max_length=255),
        ),
    ]