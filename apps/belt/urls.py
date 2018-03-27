from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.index),
    url(r'^registration$', views.reg),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^quotes$', views.quotes),
    url(r'^add$', views.add),
    url(r'^fave/(?P<id>\d+)$', views.addfave),
    url(r'^unfave/(?P<id>\d+)$', views.unfave),
    url(r'^users/(?P<id>\d+)$', views.user),
    

]