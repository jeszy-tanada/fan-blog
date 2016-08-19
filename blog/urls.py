from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name= 'post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name= 'post_detail'),
    url(r'^post/new/$', views.post_new, name= 'post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name= 'post_edit'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name= 'post_publish'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name= 'post_delete'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name= 'add_comment'),
    url(r'^comment/(?P<pk>\d+)/ok/$', views.comment_ok, name= 'comment_ok'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name= 'comment_remove'),
    url(r'^drafts/$', views.post_draft_list, name= 'post_draft_list'),
    url(r'^user/$', views.add_user, name= 'add_user'),
    #url(r'^accounts/login/$', django.contrib.auth.views.login, name=login),
]