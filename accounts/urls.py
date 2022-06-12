from django.urls import path
from .views import SignUpView, LoginView, my_account, edit_account
from django.contrib.auth.views import LogoutView

app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('my_account/', my_account, name='my_account'),
    path('edit_account/', edit_account, name='edit_account'),
    # path('update/', account_settings, name='update_account'),
    # path('profile/<uuid:pk>/update/', ProfileUpdateView.as_view(), name='update_profile')
    # path('profile/<uuid:pk>/update', update_profile, name='update_profile')
]
