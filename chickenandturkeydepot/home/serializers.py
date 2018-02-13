#i did'nt use serialiser
# i was suppose to use REST API + Ajax.. That was what required the serializer thing..
# but at the end of the day , i was able to implement it without the RESR API, APIView and all..

# i'm still keeping their files anyway.. i'll most likely delete it soon but right about now,
# i still want to have it for learning purposes...

from rest_framework import serializers
from .models import Meat

class MeatModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meat
		fields = [
			'meat_type',
			'cut_type',
			'weight',
		]

