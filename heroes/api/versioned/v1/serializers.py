from heroes import models

from rest_framework import serializers


class HeroWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeroWeapon
        fields = (
            'name',
            'image',

            'aim_type',
            'damage',
            'movement_speed',
            'rate_of_fire',
            'ammo',
            'headshot',
            'spread',
            'falloff_range',

        )


class HeroAbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HeroAbility
        fields = (
            'name',
            'image',
            'cooldown',
            'damage',
            'description',
            'type',
            'healing',
            'casting_time',
            'movement_speed',
        )


class HeroUltimateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HeroUltimate
        fields = (
            'name',
            'image',
            'aim_type',
            'cost',
            'casting_time',
            'movement_speed',
            'duration',
            'damage',
            'healing',
            'description',

        )
        ordering = ('id')


class HeroesDetailSerializer(serializers.ModelSerializer):
    abilities = HeroAbilitySerializer(many=True)
    weapon = HeroWeaponSerializer(many=True)
    ultimate = HeroUltimateSerializer()

    class Meta:
        model = models.Hero
        fields = (
            'name',
            'id',
            'image',
            'favourite_quote',

            'sound',
            'real_name',
            'affiliation',
            'age',
            'difficulty',
            'health',
            'shield',
            'armour',
            'role',
            'occupation',
            'weapon',
            'ultimate',
            'abilities',
            'preview_image',
        )


class HeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hero
        fields = (
            'id',
            'name',
            'role',
            'preview_image'
        )
