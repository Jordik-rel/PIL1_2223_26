from django.shortcuts import render,redirect
from  .models import semestre,licences,etudiant,administrations
from .forms import sems,lice1,administrat,etudiants_connexion
from django.contrib.auth import authenticate


def admins(request):
   if request.method=='POST':
        l1=lice1(request.POST)
        if l1.is_valid():
            l1.save()
        
   else:
        sem=sems()
        l1=lice1()

   return render(request,'projetept/administrateurs.html',{'lices':l1})

def etud(request):
  lice=licences.objects.filter(semestres='1',Jour_De_Cour='lundi' )
  lice1=licences.objects.filter(semestres='1',Jour_De_Cour='mardi')
  lice2=licences.objects.filter(semestres='1',Jour_De_Cour='mercredi')
  lice3=licences.objects.filter(semestres='1',Jour_De_Cour='jeudi')
  lice4=licences.objects.filter(semestres='1',Jour_De_Cour='vendredi')
  lice5=licences.objects.filter(semestres='1',Jour_De_Cour='samedi')
  return render(request,'projetept/l1.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l2(request):
  lice=licences.objects.filter(semestres='2',Jour_De_Cour='lundi' )
  lice1=licences.objects.filter(semestres='2',Jour_De_Cour='mardi')
  lice2=licences.objects.filter(semestres='2',Jour_De_Cour='mercredi')
  lice3=licences.objects.filter(semestres='2',Jour_De_Cour='jeudi')
  lice4=licences.objects.filter(semestres='2',Jour_De_Cour='vendredi')
  lice5=licences.objects.filter(semestres='2',Jour_De_Cour='samedi')
  return render(request,'projetept/l2.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})
# Create your views here.

def l3(request):
  lice=licences.objects.filter(semestres='3',Jour_De_Cour='lundi' )
  lice1=licences.objects.filter(semestres='3',Jour_De_Cour='mardi')
  lice2=licences.objects.filter(semestres='3',Jour_De_Cour='mercredi')
  lice3=licences.objects.filter(semestres='3',Jour_De_Cour='jeudi')
  lice4=licences.objects.filter(semestres='3',Jour_De_Cour='vendredi')
  lice5=licences.objects.filter(semestres='3',Jour_De_Cour='samedi')
  return render(request,'projetept/l3.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l4_im(request):
  lice=licences.objects.filter(semestres='4',Jour_De_Cour='lundi' , filiere='IM' )
  lice1=licences.objects.filter(semestres='4',Jour_De_Cour='mardi' ,filiere='IM')
  lice2=licences.objects.filter(semestres='4',Jour_De_Cour='mercredi', filiere='IM')
  lice3=licences.objects.filter(semestres='4',Jour_De_Cour='jeudi', filiere='IM')
  lice4=licences.objects.filter(semestres='4',Jour_De_Cour='vendredi', filiere='IM')
  lice5=licences.objects.filter(semestres='4',Jour_De_Cour='samedi', filiere='IM')
  return render(request,'projetept/l4_im.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l4_si(request):
  lice=licences.objects.filter(semestres='4',Jour_De_Cour='lundi' , filiere='SI' )
  lice1=licences.objects.filter(semestres='4',Jour_De_Cour='mardi' ,filiere='SI')
  lice2=licences.objects.filter(semestres='4',Jour_De_Cour='mercredi', filiere='SI')
  lice3=licences.objects.filter(semestres='4',Jour_De_Cour='jeudi', filiere='SI')
  lice4=licences.objects.filter(semestres='4',Jour_De_Cour='vendredi', filiere='SI')
  lice5=licences.objects.filter(semestres='4',Jour_De_Cour='samedi', filiere='SI')
  return render(request,'projetept/l4_si.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l4_ia(request):
  lice=licences.objects.filter(semestres='4',Jour_De_Cour='lundi' , filiere='IA' )
  lice1=licences.objects.filter(semestres='4',Jour_De_Cour='mardi' ,filiere='IA')
  lice2=licences.objects.filter(semestres='4',Jour_De_Cour='mercredi', filiere='IA')
  lice3=licences.objects.filter(semestres='4',Jour_De_Cour='jeudi', filiere='IA')
  lice4=licences.objects.filter(semestres='4',Jour_De_Cour='vendredi', filiere='IA')
  lice5=licences.objects.filter(semestres='4',Jour_De_Cour='samedi', filiere='IA')
  return render(request,'projetept/l4_ia.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l4_seiot(request):
  lice=licences.objects.filter(semestres='4',Jour_De_Cour='lundi' , filiere='SAOIT' )
  lice1=licences.objects.filter(semestres='4',Jour_De_Cour='mardi' ,filiere='SAOIT')
  lice2=licences.objects.filter(semestres='4',Jour_De_Cour='mercredi', filiere='SAOIT')
  lice3=licences.objects.filter(semestres='4',Jour_De_Cour='jeudi', filiere='SAOIT')
  lice4=licences.objects.filter(semestres='4',Jour_De_Cour='vendredi', filiere='SAOIT')
  lice5=licences.objects.filter(semestres='4',Jour_De_Cour='samedi', filiere='SAOIT')
  return render(request,'projetept/l4_seoit.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l5_im(request):
  lice=licences.objects.filter(semestres='5',Jour_De_Cour='lundi' , filiere='IM' )
  lice1=licences.objects.filter(semestres='5',Jour_De_Cour='mardi' ,filiere='IM')
  lice2=licences.objects.filter(semestres='5',Jour_De_Cour='mercredi', filiere='IM')
  lice3=licences.objects.filter(semestres='5',Jour_De_Cour='jeudi', filiere='IM')
  lice4=licences.objects.filter(semestres='5',Jour_De_Cour='vendredi', filiere='IM')
  lice5=licences.objects.filter(semestres='5',Jour_De_Cour='samedi', filiere='IM')
  return render(request,'projetept/l5_im.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l5_si(request):
  lice=licences.objects.filter(semestres='5',Jour_De_Cour='lundi' , filiere='SI' )
  lice1=licences.objects.filter(semestres='5',Jour_De_Cour='mardi' ,filiere='SI')
  lice2=licences.objects.filter(semestres='5',Jour_De_Cour='mercredi', filiere='SI')
  lice3=licences.objects.filter(semestres='5',Jour_De_Cour='jeudi', filiere='SI')
  lice4=licences.objects.filter(semestres='5',Jour_De_Cour='vendredi', filiere='SI')
  lice5=licences.objects.filter(semestres='5',Jour_De_Cour='samedi', filiere='SI')
  return render(request,'projetept/l5_si.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l5_ia(request):
  lice=licences.objects.filter(semestres='5',Jour_De_Cour='lundi' , filiere='IA' )
  lice1=licences.objects.filter(semestres='5',Jour_De_Cour='mardi' ,filiere='IA')
  lice2=licences.objects.filter(semestres='5',Jour_De_Cour='mercredi', filiere='IA')
  lice3=licences.objects.filter(semestres='5',Jour_De_Cour='jeudi', filiere='IA')
  lice4=licences.objects.filter(semestres='5',Jour_De_Cour='vendredi', filiere='IA')
  lice5=licences.objects.filter(semestres='5',Jour_De_Cour='samedi', filiere='IA')
  return render(request,'projetept/l5_ia.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l5_seiot(request):
  lice=licences.objects.filter(semestres='5',Jour_De_Cour='lundi' , filiere='SAOIT' )
  lice1=licences.objects.filter(semestres='5',Jour_De_Cour='mardi' ,filiere='SAOIT')
  lice2=licences.objects.filter(semestres='5',Jour_De_Cour='mercredi', filiere='SAOIT')
  lice3=licences.objects.filter(semestres='5',Jour_De_Cour='jeudi', filiere='SAOIT')
  lice4=licences.objects.filter(semestres='5',Jour_De_Cour='vendredi', filiere='SAOIT')
  lice5=licences.objects.filter(semestres='5',Jour_De_Cour='samedi', filiere='SAOIT')
  return render(request,'projetept/l5_seiot.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l6_im(request):
  lice=licences.objects.filter(semestres='6',Jour_De_Cour='lundi' , filiere='IM' )
  lice1=licences.objects.filter(semestres='6',Jour_De_Cour='mardi' ,filiere='IM')
  lice2=licences.objects.filter(semestres='6',Jour_De_Cour='mercredi', filiere='IM')
  lice3=licences.objects.filter(semestres='6',Jour_De_Cour='jeudi', filiere='IM')
  lice4=licences.objects.filter(semestres='6',Jour_De_Cour='vendredi', filiere='IM')
  lice5=licences.objects.filter(semestres='6',Jour_De_Cour='samedi', filiere='IM')
  return render(request,'projetept/l6_im.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l6_si(request):
  lice=licences.objects.filter(semestres='6',Jour_De_Cour='lundi' , filiere='SI' )
  lice1=licences.objects.filter(semestres='6',Jour_De_Cour='mardi' ,filiere='SI')
  lice2=licences.objects.filter(semestres='6',Jour_De_Cour='mercredi', filiere='SI')
  lice3=licences.objects.filter(semestres='6',Jour_De_Cour='jeudi', filiere='SI')
  lice4=licences.objects.filter(semestres='6',Jour_De_Cour='vendredi', filiere='SI')
  lice5=licences.objects.filter(semestres='6',Jour_De_Cour='samedi', filiere='SI')
  return render(request,'projetept/l6_si.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l6_ia(request):
  lice=licences.objects.filter(semestres='6',Jour_De_Cour='lundi' , filiere='IA' )
  lice1=licences.objects.filter(semestres='6',Jour_De_Cour='mardi' ,filiere='IA')
  lice2=licences.objects.filter(semestres='6',Jour_De_Cour='mercredi', filiere='IA')
  lice3=licences.objects.filter(semestres='6',Jour_De_Cour='jeudi', filiere='IA')
  lice4=licences.objects.filter(semestres='6',Jour_De_Cour='vendredi', filiere='IA')
  lice5=licences.objects.filter(semestres='6',Jour_De_Cour='samedi', filiere='IA')
  return render(request,'projetept/l6_ia.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})


def l6_seiot(request):
  lice=licences.objects.filter(semestres='6',Jour_De_Cour='lundi' , filiere='SAOIT' )
  lice1=licences.objects.filter(semestres='6',Jour_De_Cour='mardi' ,filiere='SAOIT')
  lice2=licences.objects.filter(semestres='6',Jour_De_Cour='mercredi', filiere='SAOIT')
  lice3=licences.objects.filter(semestres='6',Jour_De_Cour='jeudi', filiere='SAOIT')
  lice4=licences.objects.filter(semestres='6',Jour_De_Cour='vendredi', filiere='SAOIT')
  lice5=licences.objects.filter(semestres='6',Jour_De_Cour='samedi', filiere='SAOIT')
  return render(request,'projetept/l6_seiot.html',{'jours':lice,'jours1':lice1,'jours2':lice2,'jours3':lice3,'jours4':lice4,'jours5':lice5})

def licence1(request):
  return render(request,'projetept/licence1.html')

def licence2(request):
  return render(request,'projetept/licence2.html')

def licence3(request):
  return render(request,'projetept/licence3.html')

def semestre4(request):
  return render(request,'projetept/semestre4.html')

def semestre5(request):
  return render(request,'projetept/semestre5.html')

def semestre6(request):
  return render(request,'projetept/semestre6.html')

def mdp(request):
  formulaire=administrat
  mdps=administrations.objects.all()
  if request.method== 'POST':
    formulaire=administrat(request.POST)
    psw=request.POST['Mot_De_Passe']
    mdps.Mot
  return render(request,'projetept/mdp.html',{'form':formulaire})

def administration(request):
  formulaire=administrat
  message=''
  if request.method== 'POST':
     formulaire=administrat(request.POST)
     utilisateur=request.POST['Num_Matricule']
     psw=request.POST['Mot_De_Passe']
     if administrations.objects.filter(Num_Matricule=utilisateur, Mot_De_Passe=psw).exists():
       return redirect('adm')
     else:
      message='erreur, Vous n\'etes pas dans la base de donnée'
     
  return render(request,'projetept/index.html',{'etud':formulaire,'erreur':message})

def etudian(request):
  formulaire=etudiants_connexion
  if request.method== 'POST':
     formulaire=etudiants_connexion(request.POST)
     utilisateur=request.POST['Num_Matricule']
     psw=request.POST['Mot_De_Passe']
     if etudiant.objects.filter(Num_Matricule=utilisateur, Mot_De_Passe=psw).exists():
       if etudiant.objects.filter(Num_Matricule=utilisateur, Mot_De_Passe=psw , semestres='1').exists():
        return redirect('licence1')
       elif etudiant.objects.filter(Num_Matricule=utilisateur, Mot_De_Passe=psw , semestres='2').exists():
        return redirect('licence1')
       elif etudiant.objects.filter(Num_Matricule=utilisateur, Mot_De_Passe=psw , semestres='3').exists():
        return redirect('licence2')
       elif etudiant.objects.filter(Num_Matricule=utilisateur, Mot_De_Passe=psw , semestres='4').exists():
        return redirect('licence2')
       elif etudiant.objects.filter(Num_Matricule=utilisateur, Mot_De_Passe=psw , semestres='5').exists():
        return redirect('licence3')
       elif etudiant.objects.filter(Num_Matricule=utilisateur, Mot_De_Passe=psw , semestres='6').exists():
        return redirect('licence3')
     
  return render(request,'projetept/index2.html',{'etud':formulaire})