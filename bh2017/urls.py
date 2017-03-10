from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addArtist/', views.addArtist, name='addArtist'),
    url(r'^thankyou/', views.thankyou, name='thankyou'),
    url(r'^mailCheck/$', views.mailCheck, name='mailCheck'),
]