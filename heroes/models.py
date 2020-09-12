from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import FloatField
from django.db.models import PositiveIntegerField
from django.db.models import TextField
from django.db.models import URLField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Hero(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    real_name = models.TextField(max_length=256, null=True, blank=True)
    affiliation = models.TextField(max_length=100)
    age = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField()
    health = models.PositiveIntegerField()
    shield = models.PositiveIntegerField(null=True, blank=True)
    armour = models.PositiveIntegerField(null=True, blank=True)
    role = models.TextField(max_length=100)
    occupation = models.TextField(max_length=100, null=True, blank=True)
    favourite_quote = models.TextField(max_length=256, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    weapon = models.OneToOneField('heroes.HeroWeapon', null=True,
                                  blank=True, on_delete=models.CASCADE, related_name='weapon')
    ultimate = models.OneToOneField('heroes.HeroUltimate', null=True,
                                    blank=True, on_delete=models.CASCADE, related_name='ultimate')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_name_heroes_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('app_name_heroes_update', args=(self.slug,))

    def __str__(self):
        return self.name


class HeroWeapon(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(
        populate_from='name', default=None, null=True)
    weapon_type = models.TextField(max_length=100, null=True, blank=True)
    aim_type = models.TextField(max_length=100)
    damage = models.TextField(max_length=100)
    movement_speed = models.TextField(
        max_length=100, default=None, null=True, blank=True)
    rate_of_fire = models.TextField(
        max_length=100, default=None, null=True, blank=True)
    ammo = models.TextField(
        max_length=100, default=None, null=True, blank=True)
    headshot = models.TextField(
        max_length=100, default=False, null=True, blank=True)
    spread = models.TextField(
        max_length=100, default=None, null=True, blank=True)
    falloff_range = models.TextField(
        max_length=100, default=None, null=True, blank=True)
    max_range = models.TextField(
        max_length=100, default=None, null=True, blank=True)
    image = models.URLField(default=None, null=True, blank=True)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_name_heroweapon_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('app_name_heroweapon_update', args=(self.slug,))

    def __str__(self):
        return self.name


class HeroAbility(models.Model):

    # Fields
    hero = models.ForeignKey('heroes.Hero', null=True,
                             blank=True, on_delete=models.PROTECT, related_name='abilities')
    name = models.CharField(max_length=255)
    cooldown = models.TextField(max_length=100)
    image = models.URLField()
    damage = models.TextField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=100)
    type = models.TextField(max_length=100)
    healing = models.TextField(max_length=100, blank=True, null=True)
    casting_time = models.TextField(max_length=100, blank=True, null=True)
    movement_speed = models.TextField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_name_heroability_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('app_name_heroability_update', args=(self.pk,))

    def __str__(self):
        return self.name


class HeroUltimate(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    aim_type = models.TextField(max_length=100, null=True, blank=True)
    cost = models.TextField(max_length=100)
    casting_time = models.TextField(max_length=100, null=True, blank=True)
    movement_speed = models.TextField(max_length=100, null=True, blank=True)
    duration = models.FloatField()
    damage = models.TextField(max_length=100, null=True, blank=True)
    healing = models.TextField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=100)
    image = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_name_heroultimate_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('app_name_heroultimate_update', args=(self.pk,))

    def __str__(self):
        return self.name
