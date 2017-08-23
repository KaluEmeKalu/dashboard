
from django.conf.urls import url
from . import views


app_name = 'frontpage'

urlpatterns = [

    url(r'^$', views.index, {'isChinese': 'True'}, name="index"),
    url(r'^eng/$', views.index, name="zh_index"),
    url(r'^blogs/$', views. blog_list, {'isChinese': 'True'}, name="blog"),
    url(r'^blogs/eng/$', views.blog_list, name="eng_blog"),
    url(r'^blogs/(?P<pk>\d+)/$', views.blog_detail,
        {'isChinese': 'True'}, name="blog_detail"),
    url(r'^blogs/(?P<pk>\d+)/eng$', views.blog_detail, name="eng_blog_detail"),
    url(r'^save_email/', views.save_email, {'isChinese': 'True'}, name='save_email')

]
