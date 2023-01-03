from django.urls import path
from app.views import *
app_name = 'myapp'

urlpatterns = [ 
    path('first/',first,name='first'),
]