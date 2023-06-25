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
    path('savedata1/',savedata1),
    path('savedata2/',savedata2),
    path('savedata3/',savedata3),
    path('savedata4/',savedata4),
    path('dashboard/',dashboard),
    path('choice/',choice),
    path('private/',private_file),
    path('protected/',protected_file),


]