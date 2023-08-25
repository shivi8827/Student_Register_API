from django.urls import path

from customer import views

from .views import UpdateProfileAPIView, AddClassView, RegisterView, LoginView
urlpatterns = [
    path('add_class/', AddClassView.as_view(), name='add_class'),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    path('profile_update/', UpdateProfileAPIView.as_view(), name='profile'),
    
   
    
]
#shivi22@