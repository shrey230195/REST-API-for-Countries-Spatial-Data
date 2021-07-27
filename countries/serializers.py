from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import  Countries

class CountriesSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = Countries
		fields = '__all__'
		geo_field = 'geom'
