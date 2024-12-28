from django.contrib import admin
from .models import (
    HeroSection,
    Feature,
    FrequentlyAskedQuestion,
    ProcessStep,
    AboutSection,
    Service,
)


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ("position", "title", "icon_class")
    fields = ("position", "title", "description", "icon_class")
    ordering = ("position",)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title", "description", "image")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_class")
    fields = ("title", "description", "icon_class")


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_class")


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ("question",)
