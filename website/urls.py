from django.urls import path
from . import views

urlpatterns =[
    path('',views.home ,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('regiester/',views.register_user,name='register')
]

