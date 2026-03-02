from django.urls import path
from . import views 

urlpatterns = [
    # path('', home, name='home'),
    path('predict/', views.predict, name='predict'),
    #  path("result/", result, name="result"),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    
]

