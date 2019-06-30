from django.urls import path

from .views import (
    BrandDeleteAPIView,
)

urlpatterns = [
    path('<int:pk>/delete', BrandDeleteAPIView.as_view())
]
