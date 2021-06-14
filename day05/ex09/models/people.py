from django.db import models

class Peoples(models.Model):
    # class Meta:
    #     database_name = "ex01_movies"

    id = models.IntegerField(primary_key=True, serialize=True)
    name = models.TextField(unique=True, max_length=64, null=False)
    climate = models.TextField()
    diameter = models.IntegerField()
    orbital_period = models.models.models.BigIntegerField(_(""))
    population = models.DateTimeField(auto_now_add=True, null=False)
    rotation_period = models.DateField(null=False)
    surface_water = models.DateTimeField(auto_now=True, null=False)
    terrain = models.DateTimeField(auto_now=True, null=False)

    def __str__(self) -> str:
        return self.title