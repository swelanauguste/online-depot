from cart.forms import CartAddProductForm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .filters import ProductFilter
from .forms import ProductCreateForm
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


# class ProductCreateView(CreateView):
#     model = Product
#     fields = "__all__"


def product_create_form(request):
    form = ProductCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return JsonResponse({"message:": "works"})
    context = {"form": form}
    return render(request, "products/product_form.html", context)
