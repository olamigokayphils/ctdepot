from django.conf.urls import url
from home import views as core_views
#from django.urls import path



from . import views

urlpatterns = [
	url(r'^$', views.index , name='index'),
	url(r'^signup/$', core_views.signup, name='signup'),
	url(r'^meat/$', views.MeatListView.as_view(), name='meat'),
	url(r'^ctdepot/$', views.ajax123, name='ctdepot'  )


	#url(r'^list/$', views.MeatListAPIView.as_view(), name='list'),
]