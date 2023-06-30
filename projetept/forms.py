from django import forms
from .models import semestre,licences,etudiant,administrations
from django.core import validators

class sems(forms.ModelForm):
    class Meta:
        model= semestre
        fields= ['id']

class lice1(forms.ModelForm):
    class Meta:
        model= licences
        fields= ['Date_semaine','semestres','Matiere','Nom_Prenom_Prof','Heure_debut','Heure_fin','Heure_Total','Heure_Restant','Jour_De_Cour','filiere','Notification']
        widgets= {'Matiere':forms.TextInput(attrs={'class':'form-control'}),
                'Nom_Prenom_Prof':forms.TextInput(attrs={'class':'form-control'}),
                'Heure_Total':forms.TimeInput(attrs={'class':'form-control'}),
                'Heure_Restant':forms.TimeInput(attrs={'class':'form-control'}),
                'Heure_debut':forms.TimeInput(attrs={'class':'form-control'}),
                'Heure_fin':forms.TimeInput(attrs={'class':'form-control'}),
                'Notification':forms.Textarea(),
             }
        


class etudiants_connexion(forms.ModelForm):
    class Meta:
        model= etudiant
        fields= ['Num_Matricule','Mot_De_Passe']
        widgets={'Num_Matricule':forms.TextInput(attrs={'class':'form-control'}),
                'Mot_De_Passe':forms.PasswordInput(attrs={'class':'form-control'}),
                
        }
class administrat(forms.ModelForm):
     class Meta:
        model= administrations
        fields= ['Num_Matricule','Mot_De_Passe']
        widgets={'Num_Matricule':forms.TextInput(attrs={'class':'form-control'}),
                'Mot_De_Passe':forms.PasswordInput(attrs={'class':'form-control'}),
                
        }
        