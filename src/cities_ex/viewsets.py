from cities.models import City, District
from rest_framework import viewsets

from . import serializers


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List/retrieves cities data.
    """
    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List/retrieves districts data.
    """
    queryset = District.objects.all()
    serializer_class = serializers.DistrictSerializer

    def get_queryset(self):
        return self.queryset.filter(city_id=self.kwargs.get('city_pk'))
