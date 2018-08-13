from cities.models import City, District
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    region = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'region',
            'location',
        )

    def get_location(self, obj):
        return {
            'longitude': obj.location.x,
            'latitude': obj.location.y,
        }


class CityAutocompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )


class DistrictSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = District
        fields = (
            'id',
            'name',
            'city',
            'population',
        )
