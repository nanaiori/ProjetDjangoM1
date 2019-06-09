from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    resume = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = "livre"
        ordering = ['date']
        
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length=30, default="", editable=False)

    def __str__(self):
        return self.nom

