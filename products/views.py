# products/views.py
from django.shortcuts import render
from .models import Product

def product_dashboard(request):
    selected_product = request.GET.get('product')
    normalized_product = selected_product.lower().replace(" ", "") if selected_product else ""

    # Get unique product categories from the database
    product_categories = Product.objects.values_list('product_category', flat=True).distinct()

    # Map each category to its dashboard image filename
    image_map = {
        'serum': 'dashboard_images/serum.png',
        'moisturizer': 'dashboard_images/moisturizer.png',
        'sunscreen': 'dashboard_images/sunscreen.png',
        'aloveragel': 'dashboard_images/aloveragel.png',
    }

    selected_image = image_map.get(normalized_product)

    context = {
        'product_categories': product_categories,
        'selected_product': selected_product,
        'selected_image': selected_image,
    }

    return render(request, 'product_dashboard.html', context)
