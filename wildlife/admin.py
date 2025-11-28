# wildlife/admin.py
from django.contrib import admin
from .models import PropertyType, Property, Province, Taxon, Organisation, AnnualPopulation, TaxonRank

# Registering models to make them available in the Django admin
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(Province)
admin.site.register(Organisation)
admin.site.register(TaxonRank)
admin.site.register(Taxon)
admin.site.register(AnnualPopulation)
