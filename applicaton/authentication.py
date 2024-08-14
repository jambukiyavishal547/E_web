from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class UsernamePasswordAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        Authenticate the user using username and password.
        """
        username = request.headers.get('Username')
        password = request.headers.get('Password')
        
        logger.debug(f'Attempting to authenticate user: {username}')
        
        if not username or not password:
            logger.warning('Username or password not provided')
            return None  # No credentials provided, skip authentication
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            logger.error('User does not exist')
            raise AuthenticationFailed('No such user')

        if not user.check_password(password):
            logger.error('Incorrect password')
            raise AuthenticationFailed('Incorrect password')
        return (user, None)
    
    def authenticate_header(self, request):
        """
        Return a string indicating the authentication scheme.
        """
        return 'Basic'
