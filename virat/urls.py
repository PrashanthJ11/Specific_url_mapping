from django.urls import path
from virat.views import *
app_name='virat'
urlpatterns=[
    path('kohli/',kohli,name='kohli'),
]