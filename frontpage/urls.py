
from django.conf.urls import url
from . import views


app_name = 'frontpage'

urlpatterns = [

    url(r'^$', views.index, {'isChinese': 'True'}, name="index"),
    url(r'^eng/$', views.index, name="zh_index"),

]
