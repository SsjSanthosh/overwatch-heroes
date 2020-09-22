# Generated by Django 2.2.16 on 2020-09-22 13:24

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    replaces = [('heroes', '0001_initial'), ('heroes', '0002_auto_20200911_1307'), ('heroes', '0003_hero_abilites'), ('heroes', '0004_auto_20200911_1337'), ('heroes', '0005_auto_20200911_1340'), ('heroes', '0006_auto_20200911_1357'), ('heroes', '0007_auto_20200911_1358'), ('heroes', '0008_auto_20200911_1400'), ('heroes', '0009_remove_hero_abilites'), ('heroes', '0010_auto_20200912_1910'), ('heroes', '0011_heroability_preview_image'), ('heroes', '0012_auto_20200912_1916'), ('heroes', '0013_auto_20200913_1053'), ('heroes', '0014_auto_20200913_1058'), ('heroes', '0015_auto_20200913_1106'), ('heroes', '0016_auto_20200913_1109'), ('heroes', '0017_auto_20200913_1117'), ('heroes', '0018_auto_20200913_1152'), ('heroes', '0019_auto_20200913_1203'), ('heroes', '0020_auto_20200913_1214'), ('heroes', '0021_heroweapon_area_of_effect'), ('heroes', '0022_auto_20200913_1541'), ('heroes', '0023_auto_20200913_1542'), ('heroes', '0024_heroability_area_of_effect'), ('heroes', '0025_heroability_duration'), ('heroes', '0026_heroability_health'), ('heroes', '0027_hero_sound'), ('heroes', '0028_hero_overview')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroUltimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('aim_type', models.TextField(blank=True, max_length=100, null=True)),
                ('cost', models.TextField(max_length=100)),
                ('casting_time', models.TextField(blank=True, max_length=100, null=True)),
                ('movement_speed', models.TextField(blank=True, max_length=100, null=True)),
                ('duration', models.FloatField()),
                ('damage', models.TextField(blank=True, max_length=100, null=True)),
                ('healing', models.TextField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('image', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-pk',),
                'verbose_name_plural': 'Hero Ultimates',
            },
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('real_name', models.TextField(blank=True, max_length=256, null=True)),
                ('affiliation', models.TextField()),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('difficulty', models.PositiveIntegerField()),
                ('health', models.CharField(max_length=256)),
                ('shield', models.PositiveIntegerField(blank=True, null=True)),
                ('armour', models.PositiveIntegerField(blank=True, null=True)),
                ('role', models.TextField(max_length=100)),
                ('occupation', models.TextField(blank=True, null=True)),
                ('favourite_quote', models.TextField(blank=True, max_length=256, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('ultimate', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ultimate', to='heroes.HeroUltimate')),
                ('preview_image', models.TextField(blank=True, null=True)),
                ('sound', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name_plural': 'Heroes',
            },
        ),
        migrations.CreateModel(
            name='HeroWeapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name')),
                ('aim_type', models.CharField(max_length=100)),
                ('damage', models.CharField(blank=True, max_length=100, null=True)),
                ('movement_speed', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('rate_of_fire', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('ammo', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('headshot', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('spread', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('falloff_range', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('image', models.TextField(blank=True, default=None, null=True)),
                ('max_range', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('healing', models.CharField(blank=True, max_length=100, null=True)),
                ('hero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='weapon', to='heroes.Hero')),
                ('area_of_effect', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ('-pk',),
                'verbose_name_plural': 'Hero Weapons',
            },
        ),
        migrations.CreateModel(
            name='HeroAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cooldown', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.TextField()),
                ('damage', models.TextField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('type', models.TextField(max_length=100)),
                ('healing', models.TextField(blank=True, max_length=100, null=True)),
                ('casting_time', models.TextField(blank=True, max_length=100, null=True)),
                ('movement_speed', models.TextField(blank=True, max_length=100, null=True)),
                ('hero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='abilities', to='heroes.Hero')),
                ('area_of_effect', models.CharField(blank=True, max_length=256, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('health', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-pk',),
                'verbose_name_plural': 'Hero Abilites',
            },
        ),
    ]
