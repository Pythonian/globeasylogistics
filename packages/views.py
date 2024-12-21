from django.shortcuts import render



def home(request):

    template = "home.html"
    context = {}

    return render(request, template, context)


def about(request):

    template = "about.html"
    context = {}

    return render(request, template, context)


def services(request):

    template = "services.html"
    context = {}

    return render(request, template, context)


def track(request):

    template = "track.html"
    context = {}

    return render(request, template, context)


def contact(request):

    template = "contact.html"
    context = {}

    return render(request, template, context)
