from django.urls import path
from . import views

urlpatterns=[
    path('app/',views.app,name='app'),
    path('emotion/',views.emotion_detection,name='emotion_detection'),

]