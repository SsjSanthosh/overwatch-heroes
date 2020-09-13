from heroes import models

from rest_framework import serializers


class HeroWeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HeroWeapon
        fields = (
            'name',
            'aim_type',
            'damage',
            'movement_speed',
            'rate_of_fire',
            'ammo',
            'headshot',
            'spread',
            'falloff_range',
            'image',
        )


class HeroAbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HeroAbility
        fields = (
            'name',
            'cooldown',
            'image',
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
            'aim_type',
            'cost',
            'casting_time',
            'movement_speed',
            'duration',
            'damage',
            'healing',
            'description',
            'image',
        )


class HeroSerializer(serializers.ModelSerializer):
    abilities = HeroAbilitySerializer(many=True)
    weapon = HeroWeaponSerializer(many=True)
    ultimate = HeroUltimateSerializer()

    class Meta:
        model = models.Hero
        fields = (
            'id',
            'name',
            'real_name',
            'affiliation',
            'age',
            'difficulty',
            'health',
            'shield',
            'armour',
            'role',
            'occupation',
            'favourite_quote',
            'image',
            'weapon',
            'ultimate',
            'abilities', 
            'preview_image'
        )
