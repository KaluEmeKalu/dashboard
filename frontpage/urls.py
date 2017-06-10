
from django.conf.urls import url
from . import views


app_name = 'frontpage'

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^zh/$', views.index, {'isChinese': 'True'}, name="zh_index"),

]
