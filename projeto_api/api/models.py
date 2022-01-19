from django.db import models

#Model Region
class Region(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

#model Fluit
class Fluit(models.Model):
    name_fluit = models.CharField(max_length=200)
    region_fluit = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name_fluit
