# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Intervention(models.Model):
	choix_statut = (
        ('B', 'Brouillon'),
        ('V', 'Validé'),
        ('T', 'Terminé')
    )
	libelle 	= models.CharField(max_length=254, null=True)
	description = models.CharField(max_length=254, null=True)
	nom_inter 	= models.CharField(max_length=254, null=True)
	lieu		= models.CharField(max_length=254, null=True)
	date_inter	= models.DateTimeField(null=True)
	date_crea	= models.DateTimeField(auto_now_add=True)
	statut		= models.CharField(max_length=1, choices=choix_statut,null=True)
	
	def _str_(self):
		return self.libelle
