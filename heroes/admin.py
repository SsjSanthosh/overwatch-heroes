from django.contrib import admin
from .models import Hero, HeroWeapon, HeroAbility, HeroUltimate
# Register your models here.
admin.site.register(Hero)
admin.site.register(HeroWeapon)
admin.site.register(HeroAbility)
admin.site.register(HeroUltimate)
