from .models import Category


def categories(request):
    cats = Category.objects.all()
    return {'cat_menu': cats}

