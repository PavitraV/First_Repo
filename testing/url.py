from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^load$', views.loadData, name='loadData'),
    url(r'^view$', views.viewData, name='viewData'),
]