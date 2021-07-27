from django.db import models

# Create your models here.

from django.contrib.gis.db import models


class Countries(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)        
    name = models.CharField(max_length=255, primary_key = True, default= "Default")

    class Meta:
        managed = True
        db_table = 'countries'
