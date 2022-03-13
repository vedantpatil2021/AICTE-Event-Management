from participantapp import views
from django.urls import path

urlpatterns = [
    path('participantdb',views.participantdb,name="participantdb"),
    path('participantlogin',views.participantlogin,name="participantlogin"),
    path('participantcreateaccount',views.participantcreateaccount,name="participantcreateaccount"),
    path('participantevent',views.participantevent,name="participantevent"),
    path('participanteventregistration/<str:pk>',views.participanteventregistration,name="participanteventregistration"),
    path('participantgeneraldetails',views.participantgeneraldetails,name="participantgeneraldetails"),
    path('participantlogout',views.participantlogout,name="participantlogout"),
] 