from django.urls import path
from . import views

urlpatterns = [
    path('',views.endpoints),  
    path('advocates/',views.advocate_list,name='advocates'),  
    path('advocates/<str:user>/',views.AdvocateDetails.as_view()),#takes dynamic usernames
    
    #company/
    path('company/',views.company_details)
]

#these are the 3 endpoints 

#now create some database objects and serialize them