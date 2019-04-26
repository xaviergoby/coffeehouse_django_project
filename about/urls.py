from django.urls import path
from . import views


urlpatterns = [path('', views.about, name='css'),
               path('css/', views.about, name='css'),
               path('maven', views.maven, name='maven'),
               path('mro', views.mro, name='mro'),
]