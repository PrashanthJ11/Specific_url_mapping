from django.urls import path

from rohit.views import *

app_name='sharma'

urlpatterns=[
    path('sharma/',sharma,name='sharma'),
]