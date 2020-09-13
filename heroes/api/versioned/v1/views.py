from django.views.generic import DetailView, ListView, UpdateView, CreateView
from heroes.models import Hero, HeroWeapon, HeroAbility, HeroUltimate
from . import serializers
from rest_framework import viewsets, permissions, views
from rest_framework.response import Response
from heroes import models


class HeroesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Heroes class"""
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroesSerializer

class HeroesListViewSet(viewsets.ModelViewSet):
    """ViewSet for the Heroes class list"""
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroesDetailSerializer


# class HeroWeaponViewSet(viewsets.ModelViewSet):
#     """ViewSet for the HeroWeapon class"""

#     queryset = models.HeroWeapon.objects.all()
#     serializer_class = serializers.HeroWeaponSerializer


# class HeroAbilityViewSet(viewsets.ModelViewSet):
#     """ViewSet for the HeroAbility class"""

#     queryset = models.HeroAbility.objects.all()
#     serializer_class = serializers.HeroAbilitySerializer


# class HeroUltimateViewSet(viewsets.ModelViewSet):
#     """ViewSet for the HeroUltimate class"""

#     queryset = models.HeroUltimate.objects.all()
#     serializer_class = serializers.HeroUltimateSerializer
