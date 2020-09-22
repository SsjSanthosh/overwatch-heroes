from django.urls import reverse
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
    sound = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    overview = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    real_name = models.TextField(max_length=256, null=True, blank=True)
    affiliation = models.TextField()
    age = models.PositiveIntegerField(null=True, blank=True)
    difficulty = models.PositiveIntegerField()
    health = models.CharField(max_length=256)
    shield = models.PositiveIntegerField(null=True, blank=True)
    armour = models.PositiveIntegerField(null=True, blank=True)
    role = models.TextField(max_length=100)
    occupation = models.TextField(null=True, blank=True)
    favourite_quote = models.TextField(max_length=256, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    preview_image = models.TextField(blank=True, null=True)
    ultimate = models.OneToOneField('heroes.HeroUltimate', null=True,
                                    blank=True, on_delete=models.CASCADE, related_name='ultimate')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "Heroes"

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
    hero = models.ForeignKey('heroes.Hero', null=True,
                             blank=True, on_delete=models.PROTECT, related_name='weapon')
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(
        populate_from='name', default=None, null=True)
    description = models.TextField(null=True, blank=True)
    aim_type = models.CharField(max_length=100)
    damage = models.CharField(max_length=100, null=True, blank=True)
    healing = models.CharField(max_length=100, null=True, blank=True)
    movement_speed = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    rate_of_fire = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    ammo = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    headshot = models.CharField(
        max_length=100, default=False, null=True, blank=True)
    spread = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    falloff_range = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    max_range = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    image = models.TextField(default=None, null=True, blank=True)
    area_of_effect = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Hero Weapons"

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
    cooldown = models.CharField(max_length=100, null=True, blank=True)
    image = models.TextField()
    damage = models.TextField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    type = models.TextField(max_length=100)
    healing = models.TextField(max_length=100, blank=True, null=True)
    casting_time = models.TextField(max_length=100, blank=True, null=True)
    movement_speed = models.TextField(max_length=100, null=True, blank=True)
    area_of_effect = models.CharField(max_length=256, null=True, blank=True)
    duration = models.CharField(null=True, blank=True, max_length=100)
    health = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('pk',)
        verbose_name_plural = "Hero Abilites"

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
    description = models.TextField()
    image = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "Hero Ultimates"

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_name_heroultimate_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('app_name_heroultimate_update', args=(self.pk,))

    def __str__(self):
        return self.name
