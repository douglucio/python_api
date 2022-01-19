from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    #url(r'^region$', RegionList.as_view()),
    #url(r'^region/(?P<pk>[0-9]+)$', RegionDetalhes.as_view()),
    path('region', RegionList.as_view()),
    #path('region/(?P<pk>[0-9]+)$', RegionDetalhes.as_view()),    
    path('region/<int:pk>', RegionDetalhes.as_view()), 
    path('fluit', FluitList.as_view()),
    path('fluit/<int:pk>', FluitDetalhes.as_view()), 

]