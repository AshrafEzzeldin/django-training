from django.urls import path
from authentication.views import RegisterView, LoginView
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
]
