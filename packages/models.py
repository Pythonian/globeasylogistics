from django.db import models


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
