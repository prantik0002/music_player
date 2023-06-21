from django.urls import path
from music.views import *
urlpatterns=[
    path('',greeting),
    path('login/',userLogin),
    path('logout/',userLogout),
    path('signup/',signup),
    path('savedata/',savedata),
    path('file/',file),
    path('public_file/',public_file),
    path('success/',success),
    path('about/',about),
    path('contact/',contact),

]