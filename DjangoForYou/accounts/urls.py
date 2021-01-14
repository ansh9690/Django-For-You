from django.urls import path
from accounts.views import register, login_view, logout_view
app_name = 'accounts'

urlpatterns = [
    # register
    path('register/', register, name='signup'),
    # login / logout 
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
]
