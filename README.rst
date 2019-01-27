=====================================================================
 Tokenauth
=====================================================================
Tokenauth developed for django rest token authentication. It enables you to define expiration time and token prefix. Tokens generate with random data and it use SHA-256 algorithm.

Installation
============
on Pypi
::
  pip install tokenauth
on Github
::
  git clone git@github.com:ahmetkotan/tokenauth.git
  cd tokenauth
  python setup.py install

Settings
============
Added to `INSTALLED_APPS`.
::

  INSTALLED_APPS = [
      ...
      'tokenauth',
      ...
  ]

Added to `urls.py`.
::
  urlpatterns = [
      ...
      url(r'^<your-login-url>/', include('tokenauth.urls')),
      ...
]

Definition in `settings.py`
::
  TOKEN_EXPIRATION_TIME = 60 * 60 * 24 * 3 # Default 3 days
  TOKEN_PREFIX = "Bearer"
  TOKEN_REFRESH = True

Usage
=====
Definition in `settings.py`
::
  # Rest Framework
  REST_FRAMEWORK = {
      ...
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'tokenauth.auth.TokenAuthentication',
      ),
      ...
  }

Or in `views.py`
::
  from tokenauth.auth import TokenAuthentication
  class SimpleView(ModelViewset):
      authentication_classes = (TokenAuthentication, )


Created token and login:
::
  curl -X POST -H "Content-Type: application/json" -d '{"username": "<username>", "password":"<password>"}' <your-django-url>/<your-login-url>/tokens/

Refresh token:
::
  curl -X PUT -H "Content-Type: application/json" -d '{"key": "<your-valid-token>"}' <your-django-url>/<your-login-url>/tokens/

Deleted token and logout:
::
  curl -X DELETE -H "Content-Type: application/json" -H "Authorization: <your-token>" <your-django-url>/<your-login-url>/tokens/

