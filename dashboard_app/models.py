from django.db import models


class YourModel(models.Model):
    # Existing fields
    objects = None
    intensity = models.FloatField()
    likelihood = models.FloatField()
    relevance = models.FloatField()
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    topics = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # Additional fields for filters
    end_year = models.IntegerField()
    sector = models.CharField(max_length=100)
    pest = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    swot = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country} - {self.city}"
