from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name="index"),
    path('login_student/',views.login_student, name="Login_student"),
    path('login_teach/',views.login_teach, name="Login_teach"),
    path('choice/',views.choice, name="choice"),
    path('dashboard_s/',views.dashboard_s, name="Dashboard_s"),
    path('dashboard_t/',views.dashboard_t, name="Dashboard_t")

]