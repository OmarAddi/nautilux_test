from rest_framework import serializers
from models import Intervention


class IntervSerializer(serializers.ModelSerializer):

	class Meta:
		model = Intervention
		fields= '__all__'