from rest_framework import generics

from .models import Campaign
from .serializers import CampaignSerializer


class CampaignDeleteAPIView(generics.DestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
