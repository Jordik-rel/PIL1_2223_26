# Generated by Django 4.2.2 on 2023-06-25 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetept', '0006_administrateur_etudiant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrateur',
            name='Num_Matricule',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='Num_Matricule',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True),
        ),
    ]