from django.db import models

# Create your models here.
class Produit(models.Model):

    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    informations = models.TextField()

    def __str__(self):
        return self.nom
