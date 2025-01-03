import uuid
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HeroSection(TimeStampedModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    background_image = models.ImageField(upload_to="hero_images/")

    def __str__(self):
        return self.title


class Feature(TimeStampedModel):
    icon_class = models.CharField(
        max_length=255,
        help_text="FontAwesome class for the icon, e.g., 'fa-user'",
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class FrequentlyAskedQuestion(TimeStampedModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class AboutSection(TimeStampedModel):
    title = models.CharField(
        max_length=200,
        help_text="Title for the About section",
    )
    description = models.TextField(
        help_text="Main description for the About section",
    )
    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True,
        help_text="Upload an image for the About section",
    )

    def __str__(self):
        return "About Section Content"


class Service(TimeStampedModel):
    title = models.CharField(
        max_length=100,
        help_text="Service title",
    )
    description = models.TextField(
        help_text="Short description of the service",
    )
    icon_class = models.CharField(
        max_length=100,
        help_text="FontAwesome class for the icon, e.g., 'fa-truck'",
    )

    def __str__(self):
        return self.title


class ProcessStep(TimeStampedModel):
    title = models.CharField(
        max_length=100,
        help_text="Title for the process step",
    )
    description = models.TextField(help_text="Description of the process step")
    icon_class = models.CharField(
        max_length=100,
        help_text="FontAwesome class (e.g., 'fa-solid fa-person-walking')",
    )
    position = models.PositiveIntegerField(
        default=0,
        help_text="Position of the step. Lower values appear first.",
    )

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.position}. {self.title}"


class Package(TimeStampedModel):
    class PackageStatus(models.TextChoices):
        AWAITING_PICKUP = "awaiting_pickup", _("Awaiting Pickup")
        IN_TRANSIT = "in_transit", _("In Transit")
        DELIVERED = "delivered", _("Delivered")
        RETURNED = "returned", _("Returned")

    class ShipmentType(models.TextChoices):
        STANDARD = "standard", _("Standard")
        EXPRESS = "express", _("Express")
        OVERNIGHT = "overnight", _("Overnight")

    class ReturnStatus(models.TextChoices):
        NOT_RETURNED = "not_returned", _("Not Returned")
        RETURN_REQUESTED = "return_requested", _("Return Requested")
        RETURNED = "returned", _("Returned")

    title = models.CharField(
        max_length=255,
        verbose_name=_("Title"),
        help_text=_("Title of the package."),
    )
    package_uuid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name=_("Package UUID"),
        help_text=_("Unique identifier for the package."),
    )
    tracking_number = models.CharField(
        max_length=15,
        unique=True,
        editable=False,
        verbose_name=_("Tracking Number"),
        help_text=_("Unique identifier for the package."),
    )
    point_of_departure = models.CharField(
        max_length=255,
        verbose_name=_("Point of Departure"),
        help_text=_("The origin location of the package."),
    )
    receiving_address = models.CharField(
        max_length=255,
        verbose_name=_("Receiving Address"),
        help_text=_("The destination address for the package."),
    )
    estimated_delivery_date = models.DateField(
        verbose_name=_("Estimated Delivery Date"),
        help_text=_("The expected date of delivery."),
    )
    current_status = models.CharField(
        max_length=20,
        choices=PackageStatus.choices,
        default=PackageStatus.AWAITING_PICKUP,
        verbose_name=_("Current Status"),
        help_text=_("The current status of the package."),
    )
    weight = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Weight of Package"),
        help_text=_("Weight of the package in kilograms."),
    )
    dimensions = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Dimensions"),
        help_text=_("Dimensions of the package: length or width or height in cm."),
    )
    description = models.CharField(
        max_length=255,
        verbose_name=_("Package Description"),
        help_text=_("Description of the package."),
    )
    image = ProcessedImageField(
        processors=[ResizeToFill(960, 600)],
        format="JPEG",
        options={"quality": 80},
        verbose_name=_("image"),
        upload_to="package_images/",
        help_text=_("Images of the package for identification. 500kb Max"),
    )
    special_instructions = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Special Instructions"),
        help_text=_("Any special instructions for handling the package."),
    )
    shipment_type = models.CharField(
        max_length=20,
        choices=ShipmentType.choices,
        default=ShipmentType.STANDARD,
        verbose_name=_("Shipment Type"),
        help_text=_("Type of shipment."),
    )
    courier_personnel = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Courier Personnel"),
        help_text=_("Name/Identity of the person currently handling the package."),
    )
    return_status = models.CharField(
        max_length=20,
        choices=ReturnStatus.choices,
        default=ReturnStatus.NOT_RETURNED,
        verbose_name=_("Return Status"),
        help_text=_("The return processing status of the package."),
    )
    return_instructions = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Return Instructions"),
        help_text=_("Instructions for handling the package if returned."),
    )

    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")
        ordering = ["-created_at"]

    def __str__(self):
        return f"Package {self.tracking_number} - {self.current_status}"

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = self.generate_tracking_number()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_tracking_number():
        prefix = "GEL"
        unique_number = get_random_string(
            length=12,
            allowed_chars="0123456789",
        )
        return f"{prefix}{unique_number}"


class Sender(TimeStampedModel):
    sender_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Sender ID"),
        help_text=_("Unique identifier for the sender."),
    )
    package = models.ForeignKey(
        "Package",
        on_delete=models.CASCADE,
        related_name="sender_package",
        verbose_name=_("Package"),
        help_text=_("The package associated with this sender."),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Sender Name"),
        help_text=_("The full name of the sender."),
    )
    email = models.EmailField(
        verbose_name=_("Sender Email"),
        help_text=_("The email address of the sender."),
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name=_("Sender Phone Number"),
        help_text=_("The phone number of the sender."),
    )
    address = models.CharField(
        max_length=255,
        verbose_name=_("Sender Address"),
        help_text=_("The physical address of the sender."),
    )

    def __str__(self):
        return f"{self.name} - {self.email}"


class Recipient(TimeStampedModel):
    recipient_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Recipient ID"),
        help_text=_("Unique identifier for the recipient."),
    )
    package = models.ForeignKey(
        "Package",
        on_delete=models.CASCADE,
        related_name="recipient_package",
        verbose_name=_("Package"),
        help_text=_("The package associated with this recipient."),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Recipient Name"),
        help_text=_("The full name of the recipient."),
    )
    email = models.EmailField(
        verbose_name=_("Recipient Email"),
        help_text=_("The email address of the recipient."),
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name=_("Recipient Phone Number"),
        help_text=_("The phone number of the recipient."),
    )
    address = models.CharField(
        max_length=255,
        verbose_name=_("Recipient Address"),
        help_text=_("The physical address of the recipient."),
    )

    def __str__(self):
        return f"{self.name} - {self.email}"


class TrackingUpdate(TimeStampedModel):
    class PackageStatus(models.TextChoices):
        AWAITING_PICKUP = "awaiting_pickup", _("Awaiting Pickup")
        IN_TRANSIT = "in_transit", _("In Transit")
        DELIVERED = "delivered", _("Delivered")
        RETURNED = "returned", _("Returned")
        DELAYED = "delayed", _("Delayed")

    class DelayReason(models.TextChoices):
        WEATHER = "weather", _("Weather Delay")
        CUSTOMS = "customs", _("Customs Hold")
        TRAFFIC = "traffic", _("Traffic Congestion")
        MECHANICAL_ISSUE = "mechanical", _("Mechanical Issue")

    package = models.ForeignKey(
        "Package",
        on_delete=models.CASCADE,
        related_name="tracking_updates",
        verbose_name=_("Package"),
        help_text=_("The package associated with this tracking update."),
    )
    status = models.CharField(
        max_length=20,
        choices=PackageStatus.choices,
        verbose_name=_("Status"),
        help_text=_("The current status of the package."),
    )
    location = models.CharField(
        max_length=255,
        verbose_name=_("Current Location"),
        help_text=_("The last known location of the package."),
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Timestamp"),
        help_text=_("The time this update was recorded."),
    )
    delay_reason = models.CharField(
        max_length=20,
        choices=DelayReason.choices,
        blank=True,
        null=True,
        verbose_name=_("Delay Reason"),
        help_text=_("Reason for delay, if applicable."),
    )

    class Meta:
        verbose_name = _("Tracking Update")
        verbose_name_plural = _("Tracking Updates")
        ordering = ["-timestamp"]

    def __str__(self):
        return f"Update for {self.package.tracking_number} - {self.status}"

    def get_status_display_with_timestamp(self):
        return f"{self.get_status_display()} (Updated: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"


class Payment(TimeStampedModel):
    class PaymentStatus(models.TextChoices):
        PAID = "paid", _("Paid")
        UNPAID = "unpaid", _("Unpaid")

    class PaymentMethod(models.TextChoices):
        CARD = "card", _("Card")
        CASH = "cash", _("Cash")
        TRANSFER = "transfer", _("Bank Transfer")
        MOBILE_MONEY = "mobile_money", _("Mobile Money")

    package = models.OneToOneField(
        "Package",
        on_delete=models.CASCADE,
        related_name="payment",
        verbose_name=_("Package"),
        help_text=_("The package associated with this payment."),
    )
    sender_payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Sender Payment Amount"),
        help_text=_("Amount paid by the sender for shipping."),
    )
    recipient_payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Recipient Payment Amount"),
        help_text=_(
            "Amount the recipient is expected to pay before collecting the package."
        ),
    )
    invoice_number = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_("Invoice Number"),
        help_text=_("Unique invoice number for record-keeping."),
    )
    sender_payment_status = models.CharField(
        max_length=10,
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID,
        verbose_name=_("Sender Payment Status"),
        help_text=_("Payment status for the sender."),
    )
    recipient_payment_status = models.CharField(
        max_length=10,
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID,
        verbose_name=_("Recipient Payment Status"),
        help_text=_("Payment status for the recipient."),
    )
    sender_payment_method = models.CharField(
        max_length=15,
        choices=PaymentMethod.choices,
        blank=True,
        null=True,
        verbose_name=_("Sender Payment Method"),
        help_text=_("Payment method used by the sender."),
    )
    recipient_payment_method = models.CharField(
        max_length=15,
        choices=PaymentMethod.choices,
        blank=True,
        null=True,
        verbose_name=_("Recipient Payment Method"),
        help_text=_("Payment method used by the recipient."),
    )

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return f"Payment for {self.package.tracking_number} (Invoice: {self.invoice_number})"
