from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('userprofile/', views.userprofile, name = 'userprofile'),
    path('track/', views.track, name = 'track'),
    path('trigger/', views.trigger, name = 'trigger'),
    path('logout/', views.logout, name = 'logout'),
    path('tracklist/', views.tracklist, name = 'tracklist')
]