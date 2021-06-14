from django.db import models

class Movies(models.Model):
    # class Meta:
    #     database_name = "ex01_movies"

    id = models.CharField(unique=True, max_length=64, null=False)
    name = models.IntegerField(primary_key=True)
    birth_year = models.TextField(null=True)
    gender = models.CharField(null=False, max_length=32)
    eye_color = models.CharField(null=False, max_length=128)
    hair_color = models.DateField(null=False)
    height = models.DateTimeField(auto_now_add=True, null=False)
    mass = models.DateTimeField(auto_now=True, null=False)
    homeworld = models.DateTimeField(auto_now=True, null=False)

    def __str__(self) -> str:
        return self.title
    
    