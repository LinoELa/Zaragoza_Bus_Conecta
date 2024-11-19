from django.db import models

# Create your models here.



# 9 A 
class historial(models.Model):

    # modelo para que el ususarioio solo vea lo que le correspongo 

    inicio = models.CharField(max_length=50)
    final = models.CharField(max_length=50)
    
    poste_1 = models.CharField(max_length=5,null=True ,blank=True)
    poste_2  = models.CharField(max_length=5,null=True,blank=True)
    poste_3 = models.CharField(max_length=5,null=True ,blank=True)

    notas = models.CharField(max_length=500,null=True,blank=True)

    # 9 B 
    def __str__(self):
        return (f"{self.inicio} {self.final}")
    


