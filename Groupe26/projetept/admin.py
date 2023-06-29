from django.contrib import admin
from .models import licences,semestre,administrateur,etudiant,autre

@admin.register(licences)
class licences1(admin.ModelAdmin):
    list_display=('Matiere','Heure_Total')


@admin.register(autre)
class licences1(admin.ModelAdmin):
    list_display=('Jour_De_Cour','jour_semaine','filiere')

@admin.register(semestre)
class sem(admin.ModelAdmin):
    list_display=()


@admin.register(administrateur)
class administrateur(admin.ModelAdmin):
    list_display=('Num_Matricule','Mot_De_Passe')

@admin.register(etudiant)
class etudiant(admin.ModelAdmin):
    list_display=('Num_Matricule','Mot_De_Passe')
# Register your models here.
