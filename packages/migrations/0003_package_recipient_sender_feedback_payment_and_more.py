# Generated by Django 5.1.4 on 2024-12-29 08:01

import django.db.models.deletion
import imagekit.models.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_alter_herosection_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('package_uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for the package.', unique=True, verbose_name='Package UUID')),
                ('tracking_number', models.CharField(editable=False, help_text='Unique identifier for the package.', max_length=15, unique=True, verbose_name='Tracking Number')),
                ('point_of_departure', models.CharField(help_text='The origin location of the package.', max_length=255, verbose_name='Point of Departure')),
                ('receiving_address', models.TextField(help_text='The destination address for the package.', verbose_name='Receiving Address')),
                ('estimated_delivery_date', models.DateField(help_text='The expected date of delivery.', verbose_name='Estimated Delivery Date')),
                ('current_status', models.CharField(choices=[('awaiting_pickup', 'Awaiting Pickup'), ('in_transit', 'In Transit'), ('delivered', 'Delivered'), ('returned', 'Returned')], default='awaiting_pickup', help_text='The current status of the package.', max_length=20, verbose_name='Current Status')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, help_text='Weight of the package in kilograms.', max_digits=10, null=True, verbose_name='Weight of Package')),
                ('dimensions', models.TextField(blank=True, help_text='Dimensions of the package: length, width, height in cm.', null=True, verbose_name='Dimensions')),
                ('description', models.CharField(help_text='Description of the package.', max_length=255, verbose_name='Package Description')),
                ('value', models.DecimalField(blank=True, decimal_places=2, help_text='Declared value of the package for insurance purposes.', max_digits=15, null=True, verbose_name='Package Value')),
                ('image', imagekit.models.fields.ProcessedImageField(help_text='Images of the package for identification. 500kb Max', upload_to='package_images/', verbose_name='image')),
                ('special_instructions', models.TextField(blank=True, help_text='Any special instructions for handling the package.', null=True, verbose_name='Special Instructions')),
                ('insurance_coverage', models.DecimalField(blank=True, decimal_places=2, help_text='The amount covered by insurance for the package.', max_digits=15, null=True, verbose_name='Insurance Coverage')),
                ('shipment_type', models.CharField(choices=[('standard', 'Standard'), ('express', 'Express'), ('overnight', 'Overnight')], default='standard', help_text='Type of shipment.', max_length=20, verbose_name='Shipment Type')),
                ('signed_by', models.CharField(blank=True, help_text='Name of the person who signed for the package upon delivery.', max_length=255, null=True, verbose_name='Signed By')),
                ('customs_declaration', models.TextField(blank=True, help_text='Customs details for international shipments.', null=True, verbose_name='Customs Declaration')),
                ('customer_notes', models.TextField(blank=True, help_text='Specific notes or questions from the sender or recipient.', null=True, verbose_name='Customer Notes')),
                ('courier_personnel', models.CharField(blank=True, help_text='Name/Identity of the person currently handling the package.', max_length=255, null=True, verbose_name='Courier Personnel')),
                ('return_status', models.CharField(choices=[('not_returned', 'Not Returned'), ('return_requested', 'Return Requested'), ('returned', 'Returned')], default='not_returned', help_text='The return processing status of the package.', max_length=20, verbose_name='Return Status')),
                ('return_instructions', models.TextField(blank=True, help_text='Instructions for handling the package if returned.', null=True, verbose_name='Return Instructions')),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipient_id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for the recipient.', unique=True, verbose_name='Recipient ID')),
                ('name', models.CharField(help_text='The full name of the recipient.', max_length=255, verbose_name='Recipient Name')),
                ('email', models.EmailField(help_text='The email address of the recipient.', max_length=254, verbose_name='Recipient Email')),
                ('phone_number', models.CharField(help_text='The phone number of the recipient.', max_length=20, verbose_name='Recipient Phone Number')),
                ('address', models.TextField(help_text='The physical address of the recipient.', verbose_name='Recipient Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sender_id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for the sender.', unique=True, verbose_name='Sender ID')),
                ('name', models.CharField(help_text='The full name of the sender.', max_length=255, verbose_name='Sender Name')),
                ('email', models.EmailField(help_text='The email address of the sender.', max_length=254, verbose_name='Sender Email')),
                ('phone_number', models.CharField(help_text='The phone number of the sender.', max_length=20, verbose_name='Sender Phone Number')),
                ('address', models.TextField(help_text='The physical address of the sender.', verbose_name='Sender Address')),
                ('company_name', models.CharField(blank=True, help_text="The sender's company name, if applicable.", max_length=255, null=True, verbose_name='Company Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveIntegerField(blank=True, help_text='Rating for the service provided (1-5).', null=True, verbose_name='Rating')),
                ('comments', models.TextField(help_text='Additional feedback comments.', verbose_name='Comments')),
                ('submitted_at', models.DateTimeField(auto_now_add=True, help_text='The time the feedback was submitted.', verbose_name='Submitted At')),
                ('package', models.OneToOneField(help_text='The package for which feedback is provided.', on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='packages.package', verbose_name='Package')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sender_payment_amount', models.DecimalField(decimal_places=2, help_text='Amount paid by the sender for shipping.', max_digits=10, verbose_name='Sender Payment Amount')),
                ('recipient_payment_amount', models.DecimalField(decimal_places=2, help_text='Amount the recipient is expected to pay before collecting the package.', max_digits=10, verbose_name='Recipient Payment Amount')),
                ('tax_fees', models.DecimalField(blank=True, decimal_places=2, help_text='Taxes or additional fees, such as VAT or customs duties.', max_digits=10, null=True, verbose_name='Tax or Additional Fees')),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, help_text='Discount applied to the shipping cost.', max_digits=10, null=True, verbose_name='Discount Amount')),
                ('invoice_number', models.CharField(help_text='Unique invoice number for record-keeping.', max_length=50, unique=True, verbose_name='Invoice Number')),
                ('sender_payment_status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid'), ('pending', 'Pending')], default='unpaid', help_text='Payment status for the sender.', max_length=10, verbose_name='Sender Payment Status')),
                ('recipient_payment_status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid'), ('pending', 'Pending')], default='unpaid', help_text='Payment status for the recipient.', max_length=10, verbose_name='Recipient Payment Status')),
                ('sender_payment_method', models.CharField(blank=True, choices=[('card', 'Card'), ('cash', 'Cash'), ('transfer', 'Bank Transfer'), ('mobile_money', 'Mobile Money')], help_text='Payment method used by the sender.', max_length=15, null=True, verbose_name='Sender Payment Method')),
                ('recipient_payment_method', models.CharField(blank=True, choices=[('card', 'Card'), ('cash', 'Cash'), ('transfer', 'Bank Transfer'), ('mobile_money', 'Mobile Money')], help_text='Payment method used by the recipient.', max_length=15, null=True, verbose_name='Recipient Payment Method')),
                ('payment_date', models.DateTimeField(blank=True, help_text='The date and time when the payment was made.', null=True, verbose_name='Payment Date')),
                ('package', models.OneToOneField(help_text='The package associated with this payment.', on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='packages.package', verbose_name='Package')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='TrackingUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('awaiting_pickup', 'Awaiting Pickup'), ('in_transit', 'In Transit'), ('delivered', 'Delivered'), ('returned', 'Returned'), ('delayed', 'Delayed'), ('customs_hold', 'Customs Hold')], help_text='The current status of the package.', max_length=20, verbose_name='Status')),
                ('location', models.CharField(help_text='The last known location of the package.', max_length=255, verbose_name='Current Location')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='The time this update was recorded.', verbose_name='Timestamp')),
                ('delay_reason', models.CharField(blank=True, choices=[('weather', 'Weather Delay'), ('customs', 'Customs Hold'), ('traffic', 'Traffic Congestion'), ('mechanical', 'Mechanical Issue'), ('other', 'Other')], help_text='Reason for delay, if applicable.', max_length=20, null=True, verbose_name='Delay Reason')),
                ('delivery_route', models.CharField(blank=True, help_text='Information about the delivery route or vehicle.', max_length=255, null=True, verbose_name='Delivery Route')),
                ('package_handling_notes', models.TextField(blank=True, help_text='Details about handling actions like repackaging or redirection.', null=True, verbose_name='Package Handling Notes')),
                ('delivery_proof_document', models.FileField(blank=True, help_text='Scanned or digital copies of delivery confirmation documents.', null=True, upload_to='delivery_proofs/', verbose_name='Delivery Proof Document')),
                ('package', models.ForeignKey(help_text='The package associated with this tracking update.', on_delete=django.db.models.deletion.CASCADE, related_name='tracking_updates', to='packages.package', verbose_name='Package')),
            ],
            options={
                'verbose_name': 'Tracking Update',
                'verbose_name_plural': 'Tracking Updates',
                'ordering': ['-timestamp'],
            },
        ),
    ]
