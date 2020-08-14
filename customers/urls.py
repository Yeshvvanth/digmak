from django.urls import path
from . import views

app_name= "customer"

urlpatterns = [
    path('home/',views.home,name="home"),
    path('customer_profile/',views.customer_profile,name="profile"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),
]
