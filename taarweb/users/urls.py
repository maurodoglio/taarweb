from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import TaarGoogleProvider

urlpatterns = default_urlpatterns(TaarGoogleProvider)
