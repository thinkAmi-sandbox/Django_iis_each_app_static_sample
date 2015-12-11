from django.conf.urls import url
from .views import YellowIndexView

urlpatterns = [
    url(r'^$', YellowIndexView.as_view(), name='index'),
]