from django.conf.urls import url
from tokenauth.views import SimpleTokenLoginView

urlpatterns = [
    url(r'^tokens/$', SimpleTokenLoginView.as_view()),
]