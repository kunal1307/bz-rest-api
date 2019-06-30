from django.urls import path

from .views import (
    CampaignDeleteAPIView,
)

urlpatterns = [
    path('<int:pk>/delete', CampaignDeleteAPIView.as_view()),
]
