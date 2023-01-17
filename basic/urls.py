from django.urls import path
from . import views

urlpatterns = [
     path('',views.Welcome),
     path('detect',views.detecting),
]
