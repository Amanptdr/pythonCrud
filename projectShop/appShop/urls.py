
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
         path('home/', views.HomeView.as_view(), name ='home'),
         path('logout/', views.LogoutView.as_view(), name ='logout'),
         path('test/', views.Testing.as_view(), name ='test'),

         path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
         path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
         path('register/', views.RegisterView.as_view(), name='auth_register'),
     #     path('register/', views.UserRegistrationView.as_view(), name ='register')
         ]
    # path('index/', views.ApiOverview, name='home'),
    # path('create/', views.add_category, name='add-category'),
    # path('view/', views.view_category, name='view_items'),
    # path('update/<int:pk>/', views.update_category, name='update-items'),
    # path('category/<int:pk>/delete/', views.delete_category, name='delete-items'),