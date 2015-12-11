from django.conf.urls import url
from .views import GreenIndexView

urlpatterns = [
    url(r'^$', GreenIndexView.as_view(), name='index'),
]