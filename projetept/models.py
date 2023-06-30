from django.db import models
from datetime import date,datetime

class semestre(models.Model):
    ids=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')]
    id=models.CharField(max_length=1,choices=ids,primary_key=True,default=1)
    def __str__(self):
        return f'{self.id}'

class administrations(models.Model):
    Num_Matricule=models.CharField(max_length=12,unique=True,primary_key=True)
    Nom_Membre=models.CharField(max_length=20,default='')
    Prenom_Membre=models.CharField(max_length=20,default='')
    Mot_De_Passe=models.CharField(max_length=20,blank=False,default='')
    numero=models.IntegerField(blank=True) 


class etudiant(models.Model):
    Num_Matricule=models.CharField(max_length=12,unique=True,primary_key=True)
    Nom_Etudiant=models.CharField(max_length=20,default='')
    Prenom_Etudiant=models.CharField(max_length=20,default='')
    Mot_De_Passe=models.CharField(max_length=20,blank=False,default='')
    numero=models.IntegerField(blank=True)
    semestres=models.ForeignKey(semestre,on_delete=models.CASCADE) 
    
     

class licences(models.Model):
    fil=[('IM','IM'),('GL','GL'),('SI','SI'),('IA','IA'),('SAOIT','SAOIT')]
    jour=[('lundi','lundi'),('mardi','mardi'),('mercredi','mercredi'),
        ('jeudi','jeudi'),('vendredi','vendredi'),('samedi','samedi')]
    num_matricule_matiere=models.AutoField(primary_key=True)
    Matiere=models.CharField(max_length=25,default='')
    Nom_Prenom_Prof=models.CharField(max_length=25,default='')
    Heure_Total=models.IntegerField(default=1)
    Heure_Restant=models.IntegerField(default=1) 
    Heure_debut=models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    Heure_fin=models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    Notification=models.CharField(max_length=1000,default='', null=True,blank=True)
    semestres=models.ForeignKey(semestre,on_delete=models.CASCADE)  
    Jour_De_Cour=models.CharField(blank=False,max_length=12,choices=jour,default='lundi')
    Date_semaine=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    filiere=models.CharField(max_length=20,choices=fil,default='IM')
    
    
# Create your models here.
