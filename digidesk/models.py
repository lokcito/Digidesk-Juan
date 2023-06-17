from django.db import models

# Create your models here.
class Digimon(models.Model):
  name = models.CharField(max_length = 128, help_text = "Ingrese el nombre del Digimon.")
  img = models.CharField(max_length = 156, help_text = "Ingrese la imagen por favor.")
  level = models.CharField(max_length = 128, help_text = "Ingrese nivel por favor.")

  def __str__(self):
    return f"* {self.name} *"
    


  
