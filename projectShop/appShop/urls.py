
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
         path('test/', views.Testing.as_view(), name ='test'),
         path('home/', views.HomeView.as_view(), name ='home'),
         path('logout/', views.LogoutView.as_view(), name ='logout'),
         path('auth-token/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
      #    path('auth-token/', views.LoginView.as_view(), name='token_obtain_pair'),
         path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      #    path('login/refresh/',views.RefreshTokenView.as_view(),name="token_refresh"),
         path('register/', views.RegisterView.as_view(), name='auth_register'),
         ]