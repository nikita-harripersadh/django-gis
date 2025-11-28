from django.test import TestCase
from django.contrib.auth.models import User
from wildlife.models import (
    PropertyType,
    Province,
    Organisation,
    Property,
    TaxonRank,
    Taxon,
    AnnualPopulation,
)


class WildlifeModelTests(TestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create(username="tester")

        # Create basic lookup tables
        self.private_type = PropertyType.objects.create(name="Private")
        self.province = Province.objects.create(name="Province1")

        # Create organisation
        self.org = Organisation.objects.create(
            name="Org1",
            short_code="O1",
            national=True,
            province=self.province,
        )

        # Create property
        self.property = Property.objects.create(
            name="Property1",
            short_code="P1",
            province=self.province,
            property_type=self.private_type,
            organisation=self.org,
        )

        # Taxon rank
        self.rank = TaxonRank.objects.create(name="Species")

        # Taxon
        self.taxon = Taxon.objects.create(
            scientific_name="Acinonyx jubatus",
            common_name_varbatim="Cheetah",
            taxon_rank=self.rank
        )

    def test_property_creation(self):
        self.assertEqual(self.property.name, "Property1")
        self.assertEqual(self.property.province.name, "Province1")

    def test_taxon_creation(self):
        self.assertEqual(self.taxon.scientific_name, "Acinonyx jubatus")
        self.assertEqual(self.taxon.common_name_varbatim, "Cheetah")
        self.assertEqual(self.taxon.taxon_rank.name, "Species")

    def test_annual_population_auto_total(self):
        """Ensure total is automatically calculated in save()."""
        pop = AnnualPopulation.objects.create(
            year=2024,
            adult_male=10,
            adult_female=20,
            juvenile_male=5,
            juvenile_female=5,
            sub_adult_male=2,
            sub_adult_female=3,
            taxon=self.taxon,
            property=self.property,
            user=self.user,
        )

        self.assertEqual(pop.total, 45)  # 10+20+5+5+2+3

    def test_annual_population_handles_none(self):
        """Ensure None values are treated as 0."""
        pop = AnnualPopulation.objects.create(
            year=2024,
            adult_male=None,
            adult_female=None,
            juvenile_male=None,
            juvenile_female=None,
            sub_adult_male=None,
            sub_adult_female=None,
            taxon=self.taxon,
            property=self.property,
            user=self.user,
        )

        self.assertEqual(pop.total, 0)  # all None values become 0
