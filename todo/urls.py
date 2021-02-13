from django.contrib import admin 
from django.urls import path 
from todo import views 
  
urlpatterns = [ 
    #####################home_page########################################### 
    path('todo/', views.index, name="todo"), 
    ####################give id no. item_id name or item_id=i.id ############ 
    path('del/', views.remove, name="del"), 
    ######################################################################## 
] 