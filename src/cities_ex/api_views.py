from cities.models import City
from rest_framework.generics import ListAPIView

from . import serializers

__all__ = [
    'CityAutocompleteAPIView',
]


class CityAutocompleteAPIView(ListAPIView):
    serializer_class = serializers.CityAutocompleteSerializer

    def get_queryset(self):
        qs = City.objects.all()

        query = self.request.query_params.get('query', '')
        if query:
            qs = qs.filter(name_std__icontains=query, )
        return qs
