# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from models import Intervention
from serializers import IntervSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
import pytz
import datetime

class IntervViewSet(viewsets.ModelViewSet):

	queryset = Intervention.objects.all()
	serializer_class = IntervSerializer


	def create(self, request): 
		post_data = request.data
		now=datetime.datetime.now()
		statut = "V"
		for value in post_data:
			if post_data[value] is None :
				statut = "B"
				break
		if post_data['date_inter'] is not None:
			date_inter = datetime.datetime.strptime(post_data['date_inter'], '%Y-%m-%dT%H:%M:%S.%fZ')
			if(date_inter<now):
				statut = "T"
		Intervention.objects.create(libelle=post_data['libelle'], description=post_data['description'], nom_inter=post_data['nom_inter'],lieu=post_data['lieu'], date_inter=post_data['date_inter'],statut=statut)
		
		return Response(data="return data")

	def list(self, request):
		queryset = self.filter_queryset(self.get_queryset())
		for intervention in queryset:
			#import ipdb; ipdb.set_trace()

			#add Timezone to datetime
			now = pytz.utc.localize(datetime.datetime.now())
			#check if all the query are complete
			if intervention.statut == "B":
				if intervention.libelle is not None and intervention.description is not None and intervention.nom_inter is not None and intervention.lieu is not None and intervention.date_inter is not None:
					intervention.statut = "V"
					intervention.save()
			#check if the date of intervention are pasted
			if intervention.date_inter is not None:
				if(intervention.date_inter< now) :
					intervention.statut = "T"
					intervention.save()

		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)