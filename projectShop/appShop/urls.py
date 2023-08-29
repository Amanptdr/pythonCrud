
from django.urls import path
from . import views
urlpatterns = [
         path('home/', views.HomeView.as_view(), name ='home'),
         path('logout/', views.LogoutView.as_view(), name ='logout'),
         path('test/', views.Testing.as_view(), name ='test')
         ]
    # path('index/', views.ApiOverview, name='home'),
    # path('create/', views.add_category, name='add-category'),
    # path('view/', views.view_category, name='view_items'),
    # path('update/<int:pk>/', views.update_category, name='update-items'),
    # path('category/<int:pk>/delete/', views.delete_category, name='delete-items'),