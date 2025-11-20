from django.core.management.base import BaseCommand
from wildlife.models import Property, Province, Organisation, Taxon, AnnualPopulation
from django.db.models import Count, Sum, Q

class RunORM:
    # Task 1: Properties by type
    def properties_by_type(self):
        return Property.objects.filter(property_type__name__in=['Private', 'Community'])

    # Task 2: Provinces with organisations or properties
    def provinces_with_orgs_or_props(self):
        return Province.objects.filter(Q(organisation__isnull=False) | Q(property__isnull=False)).distinct()

    # Task 3: Organisation and property count per province
    def org_and_property_count(self):
        provinces = self.provinces_with_orgs_or_props()
        result = []
        for province in provinces:
            org_count = province.organisation_set.count()
            prop_count = province.property_set.count()
            result.append({
                'province': province.name,
                'organisations': org_count,
                'properties': prop_count
            })
        return result

    # Task 4: Annual population for Acinonyx Jubatus (Cheetah) in 2021
    def cheetah_population_2021(self):
        return AnnualPopulation.objects.filter(
            taxon__scientific_name='Acinonyx jubatus',
            year=2021
        ).aggregate(
            total_males=Sum('adult_male'),
            total_females=Sum('adult_female')
        )

    # Task 5: Species count for 'Zakki Property'
    def species_count_zakki(self):
        property_obj = Property.objects.get(name='Zakki Property')
        return property_obj.species_set.distinct().count()

    # Task 6: Organisation with largest total area
    def org_with_largest_area(self):
        return Organisation.objects.annotate(
            total_area=Sum('property__area')
        ).order_by('-total_area').first()

    # Task 7: Property with the most varying species
    def property_with_most_species(self):
        properties = Property.objects.annotate(
            species_count=Count('species', distinct=True)
        ).order_by('-species_count')
        return properties.first()

    # Task 8: Property with most animal count
    def property_with_most_animals(self):
        properties = Property.objects.annotate(
            animal_count=Sum('annualpopulation__total')
        ).order_by('-animal_count')
        return properties.first()

    # Task 9: Province with highest adult male count
    def province_with_highest_adult_males(self):
        provinces = Province.objects.annotate(
            total_adult_males=Sum('property__annualpopulation__adult_male')
        ).order_by('-total_adult_males')
        return provinces.first()

    # Task 10: Taxon parent and child taxon
    def taxon_parent_and_children(self, scientific_name, rank):
        taxon = Taxon.objects.get(scientific_name=scientific_name, taxon_rank__name=rank)
        parent = taxon.parent
        children = Taxon.objects.filter(parent=taxon)
        return parent, children

    # Task 11: Taxa without children (leaf taxa)
    def taxa_without_children(self):
        return Taxon.objects.filter(parent__isnull=True)

    # Task 12: Top user by annual population records
    def top_user_by_annual_population(self):
        return AnnualPopulation.objects.values('user').annotate(
            record_count=Count('id')
        ).order_by('-record_count').first()

class Command(BaseCommand):
    help = "Run ORM queries for wildlife assignment"

    def handle(self, *args, **kwargs):
        orm = RunORM()

        # Task 1: Properties by type
        result = orm.properties_by_type()
        self.stdout.write(f"Properties by type: {result}\n")

        # Task 2: Provinces with organisations or properties
        result = orm.provinces_with_orgs_or_props()
        self.stdout.write(f"Provinces with organisations or properties: {result}\n")

        # Task 3: Organisation and property count per province
        result = orm.org_and_property_count()
        self.stdout.write(f"Organisation and property count: {result}\n")

        # Task 4: Annual population for Acinonyx jubatus (Cheetah) in 2021
        result = orm.cheetah_population_2021()
        self.stdout.write(f"Cheetah population in 2021: {result}\n")

        # Task 5: Species count for 'Zakki Property'
        result = orm.species_count_zakki()
        self.stdout.write(f"Species count for 'Zakki Property': {result}\n")

        # Task 6: Organisation with largest total area
        result = orm.org_with_largest_area()
        self.stdout.write(f"Organisation with largest area: {result}\n")

        # Task 7: Property with the most varying species
        result = orm.property_with_most_species()
        self.stdout.write(f"Property with most varying species: {result}\n")

        # Task 8: Property with most animal count
        result = orm.property_with_most_animals()
        self.stdout.write(f"Property with most animals: {result}\n")

        # Task 9: Province with highest adult male count
        result = orm.province_with_highest_adult_males()
        self.stdout.write(f"Province with highest adult males: {result}\n")

        # Task 10: Taxon parent and child taxon
        scientific_name = "Acinonyx jubatus"
        rank = "Species"
        result = orm.taxon_parent_and_children(scientific_name, rank)
        self.stdout.write(f"Taxon parent and child taxa: {result}\n")

        # Task 11: Taxa without children
        result = orm.taxa_without_children()
        self.stdout.write(f"Taxa without children: {result}\n")

        # Task 12: Top user by annual population records
        result = orm.top_user_by_annual_population()
        self.stdout.write(f"Top user by annual population records: {result}\n")

