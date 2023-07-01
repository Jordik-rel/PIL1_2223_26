"""
URL configuration for Groupe26 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  projetept import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('l1/',views.etud,name='l1'),
    path('adm/',views.admins,name='adm'),
    path('l2/',views.l2,name='l2'),
    path('l3/',views.l3,name='l3'),
    path('l4_ia/',views.l4_ia,name='l4_ia'),
    path('l4_im/',views.l4_im,name='l4_im'),
    path('l4_si/',views.l4_si,name='l4_si'),
    path('l4_seiot/',views.l4_seiot,name='l4_seiot'),
    path('l5_ia/',views.l5_ia,name='l5_ia'),
    path('l5_im/',views.l5_im,name='l5_im'),
    path('l5_si/',views.l5_si,name='l5_si'),
    path('l5_seiot/',views.l5_seiot,name='l5_seiot'),
    path('l6_ia/',views.l6_ia,name='l6_ia'),
    path('l6_im/',views.l6_im,name='l6_im'),
    path('l6_si/',views.l6_si,name='l6_si'),
    path('l6_seiot/',views.l6_seiot,name='l6_seoit'),
    path('licence1/',views.licence1,name='licence1'),
    path('licence2/',views.licence2,name='licence2'),
    path('licence3/',views.licence3,name='licence3'),
    path('semsestre4/',views.semestre4,name='semestre4'),
    path('semsestre5/',views.semestre5,name='semestre5'),
    path('semsestre6/',views.semestre6,name='semestre6'),
    path('',views.administration,name='administration'),
    path('etudiant/',views.etudian,name='etudiant'),
    path('mdp/',views.mdp,name='mdp'),
  
]
