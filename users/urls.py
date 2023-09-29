from django.urls import path

from users.views import login, UserCreateView, UserUpdateView, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
]
