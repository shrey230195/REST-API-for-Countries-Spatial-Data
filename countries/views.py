from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry,Point
from rest_framework.decorators import action
from . models import  Countries
from . serializers import CountriesSerializer
from rest_framework.filters import SearchFilter


class CountriesViewSet(viewsets.ModelViewSet):
	serializer_class = CountriesSerializer
	queryset = Countries.objects.all()
	filter_backends = [SearchFilter]
	search_fields = ['$name']