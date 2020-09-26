from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'api/v1/heroes/details/?', views.HeroesListViewSet, basename="heroes-detail-view")
router.register(r'api/v1/heroes/?', views.HeroesViewSet, basename="heroes-selection-view")




urlpatterns = [
    #  urls for Django Rest Framework API
]
router = router.urls + urlpatterns
