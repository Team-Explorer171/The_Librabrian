from django.conf.urls import url
from django.urls import path, include

from App_login.views import login_view, logout_view, forget_password

app_name = 'App_login'

urlpatterns = [
    path('', login_view, name='defaultview'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('forget-passwd', forget_password, name='forget-passwd')
]
