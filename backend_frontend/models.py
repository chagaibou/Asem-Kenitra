from django.db import models

# Create your models here.

#table Evenement dans la base de données
class CategorieEvenement(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Evenement(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField()
    categorie = models.ForeignKey('backend_frontend.CategorieEvenement',on_delete=models.CASCADE,related_name='evenements')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

#table Categorie de Post dans la base de données
class CategoriePost(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#table Post dans la base de données
class Post(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    categorie = models.ForeignKey('backend_frontend.CategoriePost',on_delete=models.CASCADE,related_name='posts')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Infos_Adminisration(models.Model):
    titre = models.CharField(max_length=255)
    sous_titre = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.titre
