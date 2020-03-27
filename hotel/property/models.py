from django.db import models


property_type = (
    ('S', "sale"),
    ('R', "rent"),
)

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=50)
    property_type = models.CharField(choices=property_type, max_length=10)
    price = models.PositiveIntegerField()
    area = models.DecimalField(decimal_places=2, max_digits=8)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True)
    #location

    def __str__(self):
        return self.name