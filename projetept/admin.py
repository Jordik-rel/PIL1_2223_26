from django.contrib import admin
from .models import licences,semestre,administrations,etudiant

@admin.register(licences)
class licences1(admin.ModelAdmin):
    list_display=('Matiere','Heure_Total')


@admin.register(semestre)
class sem(admin.ModelAdmin):
    list_display=()


@admin.register(administrations)
class administrateur(admin.ModelAdmin):
    list_display=('Num_Matricule','Mot_De_Passe')

@admin.register(etudiant)
class etudiant(admin.ModelAdmin):
    list_display=('Num_Matricule','Mot_De_Passe')
# Register your models here.
