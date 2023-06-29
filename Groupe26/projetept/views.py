from django.shortcuts import render
from  .models import semestre,licences,administrateur,etudiant
from .forms import sems,lice1,autres


def admins(request):
   if request.method=='POST':
        l1=lice1(request.POST)
        aut=autres(request.POST)
        if l1.is_valid():
            l1.save()
        if aut.is_valid():
            aut.save()
        
   else:
        sem=sems()
        l1=lice1()
        aut=autres()
   return render(request,'projetept/administrateurs.html',{'lices':l1,'aut':aut})

def etud(request):
  lices=licences.objects.select_related('jour').all()
  lice=licences.objects.select_related('jour').filter(semestres='1' or '2' ,jour='lundi')
  lice1=licences.objects.select_related('jour').filter(semestres='1' or '2',jour='mardi')
  lice2=licences.objects.select_related('jour').filter(semestres='1' or '2',jour='mercredi')
  lice3=licences.objects.select_related('jour').filter(semestres='1' or '2',jour='jeudi')
  lice4=licences.objects.select_related('jour').filter(semestres='1' or '2',jour='vendredi')
  lice5=licences.objects.select_related('jour').filter(semestres='1' or '2',jour='samedi')
  return render(request,'projetept/l1.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5,'lices':lices})


# Create your views here.
