from .serializer import ProductSerializer
from .models import Product
from rest_framework import generics


class ProductListApiview(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


