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
    url(r'^restore', views.restore, name='restore'),
    url(r'^resetPass', views.resetPass, name='resetPass'),
    url(r'^errorpass', views.errorpass, name='errorpass'),
    url(r'^message/$', views.message, name='message'),
    url(r'^loadmorepartner/$', views.loadmorepartner, name='loadmorepartner'),
    url(r'^loadImg1', views.loadImg1, name='loadImg1'),
    url(r'^deleteImg1', views.deleteImg1, name='deleteImg1'),
    url(r'^loadImg2', views.loadImg2, name='loadImg2'),
    url(r'^deleteImg2', views.deleteImg2, name='deleteImg2'),
    url(r'^loadImg3', views.loadImg3, name='loadImg3'),
    url(r'^deleteImg3', views.deleteImg3, name='deleteImg3'),
    url(r'^loadImg4', views.loadImg4, name='loadImg4'),
    url(r'^deleteImg4', views.deleteImg4, name='deleteImg4'),
    url(r'^loadImg5', views.loadImg5, name='loadImg5'),
    url(r'^deleteImg5', views.deleteImg5, name='deleteImg5'),
    url(r'^loadImg6', views.loadImg6, name='loadImg6'),
    url(r'^deleteImg6', views.deleteImg6, name='deleteImg6'),
    url(r'^loadImg7', views.loadImg7, name='loadImg7'),
    url(r'^deleteImg7', views.deleteImg7, name='deleteImg7'),
    url(r'^loginJury', views.loginJury, name='loginJury'),
    url(r'^AuthJury', views.AuthJury, name='AuthJury'),
    url(r'^gallery1/$', views.gallery1, name='gallery1'),
    url(r'^gallery2/$', views.gallery2, name='gallery2'),
    url(r'^gallery3/$', views.gallery3, name='gallery3'),
    url(r'^vote1/(?P<paint_id>[0-9]+)/$', views.vote1, name='vote1'),
    url(r'^remVote1/(?P<paint_id>[0-9]+)/$', views.remVote1, name='remVote1'),
    url(r'^vote2/(?P<paint_id>[0-9]+)/$', views.vote2, name='vote2'),
    url(r'^remVote2/(?P<paint_id>[0-9]+)/$', views.remVote3, name='remVote3'),
    url(r'^vote3/(?P<paint_id>[0-9]+)/$', views.vote3, name='vote2'),
    url(r'^remVote3/(?P<paint_id>[0-9]+)/$', views.remVote3, name='remVote3'),
]
