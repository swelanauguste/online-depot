from cart.forms import CartAddProductForm
from django.db.models import Q
from django.views.generic import DetailView, ListView

from .filters import ProductFilter
from .models import Category, Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(is_available=True)

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Product.objects.filter(
                Q(product_name__icontains=query)
                | Q(category__category_name__icontains=query)
                | Q(tags__tag_name__icontains=query)
                | Q(description__icontains=query)
            ).distinct()
        else:
            return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    extra_context = {"add_to_cart_form": CartAddProductForm()}
    
