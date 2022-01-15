from django.urls import path
from django.utils.functional import unpickle_lazyobject

from .views import UserSignIn, UserSignUp

app_name = 'users'

urlpatterns = [
        path('/signin', UserSignIn.as_view(), name='user-signin'),
        path('/signup', UserSignUp.as_view(), name='user-signup')
        ]
