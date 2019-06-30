from rest_framework import generics, status
from rest_framework.response import Response

from .models import Brand
from .serializers import BrandSerializer


class BrandDeleteAPIView(generics.DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.get_campaigns().count() > 0:
            return Response("Cannot delete the brand: {} as campaigns are associated".format(instance.name.upper()),
                            status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



