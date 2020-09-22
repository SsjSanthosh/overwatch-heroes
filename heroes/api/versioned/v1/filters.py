from heroes.models import Hero
import django_filters
class HeroRoleBasedFilterSet(django_filters.FilterSet):
    class Meta:
        model = Hero 
        allow_related_reverse = False 
        fields = ('role','name','affiliation')