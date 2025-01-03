from django.shortcuts import render

from .models import (
    HeroSection,
    Feature,
    FrequentlyAskedQuestion,
    ProcessStep,
    AboutSection,
    Service,
)


def home(request):
    hero_section = HeroSection.objects.first()
    features = Feature.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()
    process_steps = ProcessStep.objects.all()
    about_section = AboutSection.objects.first()
    services = Service.objects.all()

    template = "home.html"
    context = {
        "hero_section": hero_section,
        "features": features,
        "faqs": faqs,
        "process_steps": process_steps,
        "about_section": about_section,
        "services": services,
    }

    return render(request, template, context)


def about(request):
    template = "about.html"
    context = {}

    return render(request, template, context)


def services(request):
    services = Service.objects.all()

    template = "services.html"
    context = {
        "services": services,
    }

    return render(request, template, context)


def track(request):
    template = "track.html"
    context = {}

    return render(request, template, context)
