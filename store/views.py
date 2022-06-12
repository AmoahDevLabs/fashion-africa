from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review


def home(request):
    products = Product.objects.filter(available=True)[:10]
    return render(request, 'store/home.html', {'products': products})


def store(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {'products': products})


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )

            return redirect('product', slug=slug)

    return render(request, 'store/product/product.html', {'product': product})


def product_list_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store/product/category_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__contains=query), available=True)
    return render(request, 'store/product/search.html', {'products': products, 'query': query})
