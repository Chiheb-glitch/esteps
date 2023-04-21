from django.shortcuts import render
from django.http import JsonResponse
import asyncio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import  Profile , Locations,Friend,Group,Alert
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from django.db.models import Q
from django.core import serializers
import json
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.hashers import make_password
import os
import uuid
from .serializers import ProfileSerializer

class UserListView(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     print(authentication_classes,permission_classes)
     def get(self, request, format=None):
         token = request.auth
        # Get the user associated with the token
         user = Token.objects.get(key=token.key).user
        # Print the token key and the associated user's username
         print("Token: ", token.key)
         print("User: ", user.username)
         usernames = [user.username for user in User.objects.all()]
         return Response (usernames)




class Getprofilebyid(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         myprofile=Profile.objects.get(user=user)
         id=request.data.get('profileid')
         if ( str(myprofile.id) == id):
             return Response({'message': '400'},status=status.HTTP_201_CREATED)

         profile=Profile.objects.get(id=id)

         data={"image":profile.profile_picture.url,
               "username":profile.user.username+'#'+ str(profile.user.id),
               "id":profile.id,
                "status":profile.is_online



               }
         print(data)
         return JsonResponse(data,safe=False)



class ChangeStatus(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]

     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         profile=Profile.objects.get(user=user)
         status=request.data.get('status')
         profile.is_online=status

         profile.save()
         return JsonResponse({'message': 'Changed'},safe=False)




class getstep(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]

     def get(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         profile=Profile.objects.get(user=user)
         step=profile.step



         return JsonResponse({'message': step},safe=False)

     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         profile=Profile.objects.get(user=user)
         step=request.data.get('step')
         profile.step=step



         profile.save()
         return JsonResponse({'message': step},safe=False)




class GetTheprofiledetails(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        token = request.auth
        user = Token.objects.get(key=token.key).user
        profileid = request.data.get('profileid')
        profiler=Profile.objects.get(id=profileid)
        group = Group.objects.get(name="Level 1",profile=user.profile)
        list=group.visible_to
        _list=Group.objects.get(name="Level 1",profile=profiler).visible_to
        print(_list.exists())
        y="2"
        if (list.exists()):
         for i in list.all():

            if ( i == profiler ):
                y="1"

        k={"level": y,
                "levelfrom":"2",
                "username": profiler.user.username,
                "bio":profiler.bio,
                "phone_number":profiler.phone_number,
                "house_location":profiler.house_location,
                "job_location":profiler.job_location,
                "studies_location":profiler.studies_location,
                "profile_picture":profiler.profile_picture.url,
                "is_online":profiler.is_online,
                "email": profiler.user.email,
                "id":profiler.id,}
        if (_list.exists()):
            for i in _list.all():
                if (i == user.profile):
                    k={"level": y,
                "levelfrom":"1",
                "username": profiler.user.username,
                "bio":profiler.bio,
                "profile_picture":profiler.profile_picture.url,
                "is_online":profiler.is_online,
                "id":profiler.id,
                }







        return JsonResponse({'message': k}, safe=False)








class CreateBio(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         bio = request.data.get('bio')
         profile=Profile.objects.get(user=user)
         profile.bio=bio




         profile.save()



         return JsonResponse ({'Data':'test'},safe=False)


class CreatePhoneNumber(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         phone_number = request.data.get('phone_number')
         profile=Profile.objects.get(
             user=user
             )
         profile.phone_number=phone_number,
         profile.save()

         return JsonResponse ({'Data':profile.phone_number},safe=False)



class CreateHouseLocation(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         house_location = request.data.get('house_location')
         profile=Profile.objects.get(
             user=user
             )
         profile.house_location=house_location

         profile.save()



         return JsonResponse ({'Data':profile.house_location},safe=False)


class CreateStudiesLocation(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         studies_location = request.data.get('studies_location')
         profile=Profile.objects.get(
             user=user
             )
         profile.studies_location=studies_location
         profile.save()


         return JsonResponse ({'Data':profile.studies_location},safe=False)



class CreateJobLocation(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         job_location = request.data.get('job_location')
         profile=Profile.objects.get(
             user=user
             )
         profile.job_location=job_location
         profile.save()



         return JsonResponse ({'Data':profile.job_location},safe=False)



class CreateHobbiesLocation(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         hobbies_location = request.data.get('hobbies_location')
         profile=Profile.objects.get(
             user=user,
             )
         profile.hobbies_location=hobbies_location
         profile.save()


         return JsonResponse ({'Data':profile.hobbies_location},safe=False)


class Getprofile(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def get(self, request, format=None):
         token = request.auth
        # Get the user associated with the token
         user = Token.objects.get(key=token.key).user
        # Print the token key and the associated user's username

         profile=Profile.objects.get(user=user)
         filtered_objects = Friend.objects.filter((Q(profile_from=profile) | Q(profile_to=profile)) & Q(status="accepted"))
         print(filtered_objects)
         dicts = [obj.__dict__ for obj in filtered_objects]
         for obj in dicts:
            obj.pop('_state', None)
         json_data = json.dumps(dicts)

         data={"image":profile.profile_picture.url,
               "username":user.username+'#'+ str(user.id),
               "network":dicts


               }
         print(data)
         return      JsonResponse(data,safe=False)
def generate_verification_code():
    return str(random.randint(1000, 9999))



class findprofileinvitation(APIView):
         authentication_classes = [authentication.TokenAuthentication]
         permission_classes = [permissions. IsAuthenticated]

         def post(self,request, format=None):
            token = request.auth
            user = Token.objects.get(key=token.key).user
            profile=Profile.objects.get(user=user)
            querysearch = request.data.get('querysearch')
            L=querysearch.split('#')
            profiles = Profile.objects.get((Q(user__id=L[1]) & Q(user__username=L[0]) ))

            requests=Friend.objects.filter(Q(profile_to=profile) | Q(profile_from=profile))
            print(requests)
            y={'data':{"username":profiles.user.username,
                               "id":profiles.id,
                               "image":profiles.profile_picture.url
                               },
                       'is_requesting':False
                       }
            for  x in requests:
                print(x.profile_from)
                if (x.profile_from.id == profiles.id or  x.profile_to.id == profiles.id  )  :
                    y={'data':{"username":profiles.user.username,
                               "id":profiles.id,
                               "image":profiles.profile_picture.url
                               },
                       'is_requesting':True,
                       "status":x.status }
                    if  (x.status == 'pending'):

                      y={'data':{"username":profiles.user.username,
                               "id":profiles.id,
                               "image":profiles.profile_picture.url
                               },
                       'is_requesting':True,
                       "status":[x.status,'To'] }
                      if (x.profile_from.id == profiles.id):
                         y={'data':{"username":profiles.user.username,
                               "id":profiles.id,
                               "image":profiles.profile_picture.url
                               },
                       'is_requesting':True,
                       "status":[x.status,'From'] }


            return JsonResponse( y ,safe=False)


class Sendinvitation(APIView):
         authentication_classes = [authentication.TokenAuthentication]
         permission_classes = [permissions. IsAuthenticated]

         def post(self,request, format=None):
            token = request.auth
            user = Token.objects.get(key=token.key).user
            profile=Profile.objects.get(user=user)
            idprofile = request.data.get('idprofile')
            profileto = Profile.objects.get(id=idprofile)

            f=Friend()
            f.profile_from=profile
            f.profile_to=profileto
            f.status='pending'


            f.save()
            return JsonResponse({'message': 'Invitation sent'}, safe=False)






class Getrequestlist(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def get(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user

         profile=Profile.objects.get(user=user)
         requests=Friend.objects.filter(Q(profile_to=profile) & Q(status="pending"))

         t=[]
         y={}
         for  x in requests:
            y={"id":x.profile_from.id,
                "username":x.profile_from.user.username +'#'+str(x.profile_from.user.id) ,
                "image":x.profile_from.profile_picture.url
               }
            t.append(y)


         return      JsonResponse({"data":t,"count":len(t)},safe=False)
     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         print(json.loads(request.body.decode('utf-8')))
         id=json.loads(request.body.decode('utf-8'))["id"]
         profile_to=Profile.objects.get(user=user)
         profile_from=Profile.objects.get(id=id)
         requests=Friend.objects.get(Q(profile_to=profile_to) & Q(profile_from=profile_from))

         if  json.loads(request.body.decode('utf-8'))["action"]  == "accepted" :
          requests.status="accepted"
          group = Group.objects.get(name="Level 1",profile=profile_from)
          group.visible_to.add(profile_to)
          group.save()
          group = Group.objects.get(name="Level 1",profile=profile_to)
          group.visible_to.add(profile_from)
          group.save()
          requests.save()
         else:
          requests.status="rejected"
          requests.save()

         print(requests)



         return JsonResponse(id,safe=False)




class Appendlevel(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]

     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         print(json.loads(request.body.decode('utf-8')))
         id=json.loads(request.body.decode('utf-8'))["id"]
         level=json.loads(request.body.decode('utf-8'))["level"]
         profile_to=Profile.objects.get(user=user)
         profile_from=Profile.objects.get(id=id)
         if (level== "Level 1"):
             group = Group.objects.get(name="Level 2",profile=profile_to)
             group.visible_to.remove(profile_from)
             group.save()

         if (level== "Level 2"):
             group = Group.objects.get(name="Level 1",profile=profile_to)
             group.visible_to.remove(profile_from)
             group.save()
         group = Group.objects.get(name=level,profile=profile_to)
         group.visible_to.add(profile_from)
         group.save()



         return JsonResponse({'message': 'level changed successfully'}, status=status.HTTP_201_CREATED)



class Alertreceiver(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]

     def get(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user

         t=[]
         alertreceiver=Profile.objects.get(user=user)
         alerts = Alert.objects.all()
         for alert in alerts:
             if alertreceiver in alert.alert_receiver.all():
                 y={"alert_sender_username":alert.alert_sender.user.username,"alert_id":str(alert.id),"alert_date":alert.alert_date,"alert_bio":alert.alert_bio,"profile_picture":alert.alert_sender.profile_picture.url,
                 "checked":alert.checked,
                 "status":alert.alert_sender.is_online
                 }
                 t.append(y)






         return JsonResponse({"data":t}, safe=False)





class checkedalert(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]

     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         id=json.loads(request.body.decode('utf-8'))["id"]
         alert=Alert.objects.get(id=id)
         if user.profile in alert.alert_receiver.all():
             alert.checked=True
             alert.save()






         return JsonResponse({"data":"sa7it"}, safe=False)



class createalert(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]

     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         bio=json.loads(request.body.decode('utf-8'))["alert_bio"]
         date=json.loads(request.body.decode('utf-8'))["date"]

         alert=Alert()
         alert.alert_sender=user.profile
         alert.alert_date=date
         alert.alert_bio=bio
         alert.alert_latitude="0"
         alert.alert_longitude="0"
         alert.save()
         group=Group.objects.get(name="Level 2",profile=user.profile)
         if (group.visible_to.exists()):

             for i in group.visible_to.all():
                 print(i)
                 if not(i == user.profile):
                     alert.alert_receiver.add(i)









         return JsonResponse({"data":"sa7it"}, safe=False)






class Register(APIView):

         def post(self,request, format=None):
           username = request.data.get('username')
           lastname = request.data.get('lastname')
           email = request.data.get('email')
           password = request.data.get('password')
           if User.objects.filter(username=username).exists():
               return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
           user = User.objects.create(
               username=username,
               last_name=lastname,
               email=email,
               password=make_password(password)
               )

           user.save()
           profile=Profile.objects.create(user=user)
           profile.save()
           group1=Group.objects.create(name="Level 1",profile=profile)
           group2=Group.objects.create(name="Level 2",profile=profile)
           group1.save()
           group2.save()
           return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)





class CreateProfile(APIView):

     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions. IsAuthenticated]
     def post(self, request, format=None):
         token = request.auth
         user = Token.objects.get(key=token.key).user
         profile_picture = request.FILES.get('image')

         if profile_picture :
             image_data=profile_picture.read()
             print("da")
             file_name=str(uuid.uuid4()) + '.png'
             profile=Profile.objects.get(user=user)
             profile.profile_picture=profile_picture

             profile.save()





         return JsonResponse ({"test":"trueee"},safe=False)








def login(request):

   # my_list = list(user.values())
    username = request.GET.get('username')
    password = request.GET.get('pwd')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        response_data = {'status': 200 , 'message': user.id}
    else:
        response_data = {'status': 404 , 'message': "wrong"}










    print('test')
    return JsonResponse(response_data,safe=False)


def get_profile(request):
        id = request.GET.get('id')
        user=User.objects.get(id=id)

        profile=Profile.objects.get(user=user)

        p={'username':user.username, 'photo' : profile.profile_picture.url,
           'role':profile.role
           }

        return JsonResponse( p ,safe=False);


def change_location(request):

     id= request.GET['id']
     la = request.GET['la']
     lo = request.GET['lo']


     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     locations=Locations.objects.get(profile=profile)
     locations.latitude=la
     locations.longitude=lo
     locations.save()

     return JsonResponse({"wored":1},safe=False)

def get_location(request):
     id=request.GET['id']
     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     locations=Locations.objects.get(profile=profile)

     return JsonResponse({"latitude":locations.latitude,"longitude":locations.longitude},safe=False)



