from django.urls import include, path
from rest_framework_nested import routers

from . import viewsets
from . import api_views

app_name = 'cities'

router = routers.SimpleRouter()
router.register(
    r'cities',
    viewsets.CityViewSet,
)

districts_router = routers.NestedSimpleRouter(
    router,
    r'cities',
    lookup='city',
)
districts_router.register(
    r'districts',
    viewsets.DistrictViewSet,
)

app_patterns = [
    path('', include(router.urls)),
    path('', include(districts_router.urls)),
    path(
        'cities/autocomplete/',
        api_views.CityAutocompleteAPIView.as_view(),
        name='cities-autocomplete'
    ),
]

urlpatterns = [
    path('v1/', include(app_patterns)),
]
