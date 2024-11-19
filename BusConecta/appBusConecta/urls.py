
from django.urls import path 
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path("inicio", views.inicio, name="inicio"),

    path("login/", views.login_user, name='login'),

    path("logout/",views.logout_user, name='logout'),

    path("register/",views.register_user, name="register"),

    path('modelos/<int:pk>', views.modelos_user, name='modelos'),

    path('borrar/<int:pk>', views.borrar_user, name='borrar'),

    path('agregar', views.agregar_user, name='agregar'),
    
    path('actualizar/<int:pk>', views.actualizar_user, name='actualizar'),
]
