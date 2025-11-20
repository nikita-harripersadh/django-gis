from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PropertyType(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property type'
        verbose_name_plural = 'Property types'
        db_table = 'property_type'


class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'
        db_table = 'province'


class Organisation(models.Model):
    """Organisation model."""
    name = models.CharField(unique=True, max_length=250)
    short_code = models.CharField(max_length=50, null=False, blank=True)
    national = models.BooleanField(null=True, blank=True)
    province = models.ForeignKey(
        Province,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )


class Property(models.Model):
    """Property model."""
    name = models.CharField(max_length=300, unique=True)
    short_code = models.CharField(max_length=50, null=False, blank=True)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    property_type = models.ForeignKey(PropertyType, on_delete=models.DO_NOTHING)
    organisation = models.ForeignKey(Organisation, on_delete=models.DO_NOTHING)

    # Use Django's built-in JSONField
    centroid = models.JSONField(null=True, blank=True)


class TaxonRank(models.Model):
    """Taxon rank model."""
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Taxon Rank"
        verbose_name_plural = "Taxon Ranks"


class Taxon(models.Model):
    """Taxon model"""
    scientific_name = models.CharField(max_length=250, unique=True)
    common_name_varbatim = models.CharField(max_length=250, null=True, blank=True)
    taxon_rank = models.ForeignKey(
        TaxonRank, on_delete=models.CASCADE, null=True, blank=True
    )
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.scientific_name


class AnnualPopulation(models.Model):
    """Annual Population model."""
    year = models.PositiveIntegerField()
    total = models.IntegerField()
    adult_male = models.IntegerField(null=True, blank=True)
    adult_female = models.IntegerField(null=True, blank=True)
    juvenile_male = models.IntegerField(null=True, blank=True)
    juvenile_female = models.IntegerField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    taxon = models.ForeignKey(Taxon, on_delete=models.CASCADE, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    area_available_to_species = models.FloatField(default=0.0)
    sub_adult_total = models.IntegerField(null=True, blank=True)
    sub_adult_male = models.IntegerField(null=True, blank=True)
    sub_adult_female = models.IntegerField(null=True, blank=True)
    juvenile_total = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.property.name, self.year)

def create_sample_data():
    # Create Property Types
    private_type = PropertyType.objects.create(name="Private")
    community_type = PropertyType.objects.create(name="Community")

    # Create Provinces
    province1 = Province.objects.create(name="Province1")
    province2 = Province.objects.create(name="Province2")

    # Create Organisations
    org1 = Organisation.objects.create(name="Org1", short_code="O1", national=True, province=province1)
    org2 = Organisation.objects.create(name="Org2", short_code="O2", national=False, province=province2)

    # Create Properties
    prop1 = Property.objects.create(name="Property1", property_type=private_type, province=province1, organisation=org1)
    prop2 = Property.objects.create(name="Property2", property_type=community_type, province=province2, organisation=org2)

    # Create Taxon Ranks
    species_rank = TaxonRank.objects.create(name="Species")
    genus_rank = TaxonRank.objects.create(name="Genus")

    # Create Taxons (Species & Genus)
    taxon1 = Taxon.objects.create(scientific_name="Acinonyx jubatus", common_name_varbatim="Cheetah", taxon_rank=species_rank)
    taxon2 = Taxon.objects.create(scientific_name="Panthera leo", common_name_varbatim="Lion", taxon_rank=species_rank)

    # Create Annual Population Records
    AnnualPopulation.objects.create(
        year=2021, total=50, adult_male=20, adult_female=30, taxon=taxon1, property=prop1, user=None)
    AnnualPopulation.objects.create(
        year=2021, total=70, adult_male=35, adult_female=35, taxon=taxon2, property=prop2, user=None)