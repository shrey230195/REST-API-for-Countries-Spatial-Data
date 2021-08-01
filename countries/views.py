from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, Polygon
from rest_framework.decorators import action
from . models import  Countries
from . serializers import CountriesSerializer, CountriesSerializerWithoutGeom
from rest_framework.filters import SearchFilter
import requests
import json
from django.db import IntegrityError
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


class CountriesViewSet(viewsets.ModelViewSet):
	serializer_class = CountriesSerializer
	queryset = Countries.objects.all()
	filter_backends = [SearchFilter]
	search_fields = ['$name']
	pagination_class = PageNumberPagination

	@action(detail=False, methods=['post'], serializer_class=CountriesSerializerWithoutGeom)
	def get_neighbor_countries(self, request):
		lookup_country = self.request.POST.get('name')
		if not lookup_country:
    			return Response({}, status=status.HTTP_200_OK)
		countries = Countries.objects.filter(name=lookup_country)
		neigbors = Countries.objects.filter(geom__touches=countries[0].geom)		
		serialized = CountriesSerializerWithoutGeom(neigbors, many = True)
		return Response(serialized.data, status=status.HTTP_200_OK)

	@action(detail=False, methods=['get'])
	def load_data(self, request):				
		data = requests.get('https://datahub.io/core/geo-countries/r/0.geojson')
		# print list of all resources:
		json_data = data.json()				
		for item in json_data["features"]:
			geom_str = json.dumps(item["geometry"])
			geom = GEOSGeometry(geom_str)
			if isinstance(geom, Polygon):
				geom = MultiPolygon([geom])
			try:
				Countries.objects.create(					
					name=item["properties"]["ADMIN"],
					geom=geom					
				)
			except IntegrityError as error:
				print("entry already exists, skipping")
				print(error)				
		
		print("addedd successfullly")
		return Response({}, status=status.HTTP_200_OK)