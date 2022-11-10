from django.urls import path
from liveapp import views

urlpatterns=[
    path("",views.Navbar,name="home"),
    path("form/",views.Register,name='form'),
    path("data/",views.Data,name="data"),
    path("delete/<int:id>/",views.Delete,name="delete"),
    path('update/<int:id>/',views.Update,name="update"),
    path('signup/',views.SignUp,name='signup'),
    path('logged/',views.LogIn,name="logged"),
    path('loggout/',views.Log_Out,name='loggout')
]