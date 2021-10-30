
from django.urls import path
from.import views

urlpatterns = [

    path('', views.lgn),
    path ('ad',views.ad,name='adm' )
]