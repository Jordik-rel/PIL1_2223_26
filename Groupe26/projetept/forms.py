from django import forms
from .models import semestre,licences,administrateur,etudiant,autre
from django.core import validators

class sems(forms.ModelForm):
    class Meta:
        model= semestre
        fields= ['id']

class lice1(forms.ModelForm):
    class Meta:
        model= licences
        fields= ['Matiere','Nom_Prenom_Prof','Heure_Total','Heure_Restant','Heure_debut','Heure_fin','semestres','jour','Notification']
        widgets= {'Matiere':forms.TextInput(attrs={'class':'form-control'}),
                'Nom_Prenom_Prof':forms.TextInput(attrs={'class':'form-control'}),
                'Heure_Total':forms.DateInput(attrs={'class':'form-control'}),
                'Heure_Restant':forms.DateInput(attrs={'class':'form-control'}),
                'Heure_debut':forms.DateInput(attrs={'class':'form-control'}),
                'Heure_fin':forms.DateInput(attrs={'class':'form-control'}),
                'Notification':forms.Textarea(),
                 }
        
class autres(forms.ModelForm):
    class Meta:
        model= autre
        fields=['Jour_De_Cour','jour_semaine','filiere']
        
        