from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addArtist/', views.addArtist, name='addArtist'),
    url(r'^thankyou/', views.thankyou, name='thankyou'),
    url(r'^mailCheck/$', views.mailCheck, name='mailCheck'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^prizes/$', views.prizes, name='prizes'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^jury/$', views.jury, name='jury'),
    url(r'^sponsors/$', views.sponsors, name='sponsors'),
    url(r'^partners/$', views.partners, name='partners'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^forgetpass/$', views.forgetpass, name='forgetpass'),
    url(r'^login/', views.loginAuth, name='loginAuth'),
    url(r'^logoutArtist', views.logoutArtist, name='logoutArtist'),
    url(r'^loginFail', views.loginFail, name='loginFail'),
    url(r'^fullArtistAdd', views.fullArtistAdd, name='fullArtistAdd'),
    url(r'^cabinet', views.cabinet, name='cabinet'),
    url(r'^changeArtist', views.changeArtist, name='changeArtist'),
    url(r'^changePassword', views.changePassword, name='changePassword'),
]