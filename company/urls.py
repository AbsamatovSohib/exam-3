from django.urls import path
from .views import ProductListApiview


urlpatterns = [
    path("list/", ProductListApiview.as_view())
]
