from .models import Information


def contact(request):
    return {"contact": Information.objects.first()}
