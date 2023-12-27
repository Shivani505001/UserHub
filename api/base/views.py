from django.shortcuts import render,redirect
from django.http import JsonResponse 
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Advocate,Company
from .serializer import advocatedserializer,companyserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from django.db.models import Q
# Create your views here.

@api_view(['GET'])
def endpoints(requests):#here requests is an object
    data = ['/advocates','/advocates:user']
    #return JsonResponse(data,safe=False) 
#In Django, the JsonResponse class is used to return JSON-encoded responses from a view function 
#safe = true allows python dic ,ie converts to json 
#safe=true  won't take python object for that we need to do serialization
    return Response(data)


@api_view(['GET','POST'])
# @permission_classes(IsAuthenticated)
def advocate_list(request):
    # data=['dennis','tadas','max']
    #advocates=Advocate.objects.all() #django has a built in orm
    #we are calling the object's method
    #return Response(advocates) - here Response can't chamge python objects 
    if request.method== 'GET':
        #FOR SEARCHING
        query=request.GET.get('query')
        if query==None:
            query=''
        advocates=Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query)) #__icontains - need exact letter, __contains - this will search with any letter [no caps , no order required]
        #Q is used for complex query searches. Here in above the search can be performed either with matching any word in bio or letter in username
        serializer=advocatedserializer(advocates,many=True) 
        #inside this advocateserializer I am putting the var which has the data 
        #that should be serialized and this class has data about what all feilds needed to be serialized 
        #finally : many =  True shows that serializing multiple objects
        return Response(serializer.data) 
    #above serializer is a classinstance and we r getting data attribute from it
    
    if request.method=='POST': #to add new user
        advocates=Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer=advocatedserializer(advocates,many=False)
        return Response(serializer.data)
        

# @api_view(['GET','PUT','DELETE'])
# def advocate_details(request,user):
#     advocates=Advocate.objects.get(username=user)
#     if request.method=='GET':
#         #/advocates/dennis/
#         serializer=advocatedserializer(advocates,many=False)
#         return Response(serializer.data)
#     if request.method=='PUT':#to update
#         advocates.username=request.data['username']
#         advocates.bio=request.data['bio']
#         advocates.save()
#         serializer=advocatedserializer(advocates,many=False)
#         return Response(serializer.data)
#     if request.method=='DELETE':
#         advocates.delete()
#         return Response('DONE')

#class based view:

class AdvocateDetails(APIView):
    
    def get_object(self,user):
        try:
            return Advocate.objects.get(username=user)
        except Advocate.DoesNotExist:
            raise JsonResponse("username doesnot exist")
           
    def get(self,request,user):#class based views have built in func . here it takes only get requests
        advo=self.get_object(user)
        serilaizer=advocatedserializer(advo)
        return Response(serilaizer.data)

    def put(self,request,user,bio):
        advo=self.get_object(user)
        advo.username=request.data['username']
        advo.bio=request.data['bio']
        serializer=advocatedserializer(advo,many=False)
        return Response(serializer.data)
    
    def delete(self,request,user):
        advoDelete=self.get_object(user)
        advoDelete.save()
        return Response("deleted")
    
#views for company
#company/

@api_view(['GET'])
def company_details(request)  :
    comp = Company.objects.all()
    serializer=companyserializer(comp,many=True)
    return Response(serializer.data)