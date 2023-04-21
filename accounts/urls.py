from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='UserListView'),
            path('getstep', views.getstep.as_view(), name='getstep'),
    path('CreateBio', views.CreateBio.as_view(), name='CreateBio'),
    path('CreatePhoneNumber', views.CreatePhoneNumber.as_view(), name='CreatePhoneNumber'),
    path('CreateHouseLocation', views.CreateHouseLocation.as_view(), name='CreateHouseLocation'),
    path('CreateStudiesLocation', views.CreateStudiesLocation.as_view(), name='CreateStudiesLocation'),
    path('CreateJobLocation', views.CreateJobLocation.as_view(), name='CreateJobLocation'),
    path('CreateHobbiesLocation', views.CreateHobbiesLocation.as_view(), name='CreateHobbiesLocation'),

    path('getrequestlist', views.Getrequestlist.as_view(), name='Getrequestlist'),
    path('register', views.Register.as_view(), name='register'),
    path('getprofileid', views.Getprofilebyid.as_view(), name='Getprofilebyid'),
    path('ChangeStatus', views.ChangeStatus.as_view(), name='ChangeStatus'),
    path('findprofileinvitation', views.findprofileinvitation.as_view(), name='findprofileinvitation'),
    path('Sendinvitation', views.Sendinvitation.as_view(), name='Sendinvitation'),
    path('Appendlevel', views.Appendlevel.as_view(), name='Appendlevel'),

    path('CreateProfile', views.CreateProfile.as_view(), name='CreateProfile'),
    path('GetTheprofiledetails', views.GetTheprofiledetails.as_view(), name='GetTheprofiledetails'),

    path('Alertreceiver', views.Alertreceiver.as_view(), name='Alertreceiver'),
    path('checkedalert', views.checkedalert.as_view(), name='CreateHobbiesLocation'),
    path('createalert', views.createalert.as_view(), name='createalert'),

    path('login', views.login, name='login'),
     path('getprofile', views.Getprofile.as_view(), name='get_profile'),
path('change_location', views.change_location, name='change_location'),
path('get_location', views.get_location, name='get_location'),
]