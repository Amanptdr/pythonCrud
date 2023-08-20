
from django.urls import path
from . import views
 
urlpatterns = [
    path('index/', views.ApiOverview, name='home'),
    path('create/', views.add_category, name='add-category'),
    path('view/', views.view_category, name='view_items'),
    path('update/<int:pk>/', views.update_category, name='update-items'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete-items'),

]