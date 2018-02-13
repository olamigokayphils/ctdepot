from django.shortcuts import render, redirect
from django.http import HttpResponse ,JsonResponse
# Create your views here.
from .models import Meat
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse #i'm not sure about this yet

from rest_framework import generics
from .serializers import MeatModelSerializer

import json

def index(request):
	number_of_meat = Meat.objects.all().count()
	mm = Meat.objects.all()

	return render(
		request,
		'index.html',
		context= {'number_of_meat' : number_of_meat},

	)


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return redirect('login')

	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form' : form})


@login_required
def ctdepot(request):
	number_of_meat = Meat.objects.all().count()

	return render(
		request,
		'ctdepot.html',
		context= {'number_of_meat' : number_of_meat},
	)



class MeatListView(generic.ListView):
	model = Meat 

#class MeatListAPIView(generics.ListAPIView):
#	queryset = Meat.objects.all().order_by('sort')
	
#	def get_serializer_class(queryset):
#		return queryse

def ajax123(request):
	if request.is_ajax:
		arr=[]
		query = Meat.objects.all().order_by('id')
		for values in query:
			dict={}
			dict['data1']=values.meat_type
			dict['data2']=values.cut_type
			dict['data3']=values.weight
			arr.append(dict)			

		return JsonResponse(json.dumps(arr),safe=False)