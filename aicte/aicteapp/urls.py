from aicteapp import views
from django.urls import path

urlpatterns = [
    path('',views.home, name="home"),
    path('coordinatordb',views.coordinatordb, name="coordinatordb"),
    path('coordinatorevent',views.coordinatorevent, name="coordinatorevent"),
    path('coordinatorprofile',views.coordinatorprofile, name="coordinatorprofile"),
    path('coordinatorbooking',views.coordinatorbooking, name="coordinatorbooking"),
    path('coordinatorcanteen',views.coordinatorcanteen, name="coordinatorcanteen"),
    path('coordinatorreport',views.coordinatorreport, name="coordinatorreport"),
    path('coordinatoreventform',views.coordinatoreventform, name="coordinatoreventform"),
    path('bookingform/<str:pk>',views.bookingform, name="bookingform"),
    path('canteenform',views.canteenform, name="canteenform"),
    path('signup',views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
    path('logout',views.logout, name="logout"),
    # path('updatecoordinatorprofile/<str:username>',views.updatecoordinatorprofile, name="updatecoordinatorprofile"),
    path('eventupdateform/<str:pk>',views.eventupdateform, name="eventupdateform"),
]   