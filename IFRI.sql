#CREATE DATABASE ecole
USE ecole;
CREATE TABLE etudiantL1(id_etudiantL1 INT PRIMARY KEY,nom VARCHAR(50),penom VARCHAR(50),email VARCHAR(100));
CREATE TABLE etudiantL2(id_etudiantL2 INT PRIMARY KEY,nom VARCHAR(50),penom VARCHAR(50),email VARCHAR(100));
CREATE TABLE etudiantL3(id_etudiantL3 INT PRIMARY KEY,nom VARCHAR(50),penom VARCHAR(50),email VARCHAR(100));
CREATE TABLE professeur(id_professeur INT PRIMARY KEY,non VARCHAR(50),penom VARCHAR(50),email VARCHAR(100));
CREATE TABLE connexion(id_utilisateur INT PRIMARY KEY, type_utilisateur ENUM('etudiant','professeur'),nom_utilisateur VARCHAR(50),mot_de_passe VARCHAR(50));
CREATE TABLE ADMINS(id_admin INT PRIMARY KEY, nom VARCHAR(50), prenom VARCHAR(50),email VARCHAR(50), mot_de_passe VARCHAR(50));
CREATE TABLE emplois_du_temps(id VARCHAR(20) PRIMARY KEY, dates datetime,matière VARCHAR(100), id_professeur VARCHAR(20), nom_professeur VARCHAR(20), prenom_professeur VARCHAR(20),durée int);


       

      
      
    
       
      
      
      
      


