from django.conf.urls.defaults import *
urlpatterns = patterns('main.views',
    url(r'^$', 'users', name='users'),
        url(r'^add/user/$', 'add_user',name='add_user'),
        url(r'^add/tweet/$', 'add_tweet',name='add_tweet'),
        url(r'^edit/user/(?P<pk>\d+)$', 'edit_user', name='edit_user'),   
		url(r'^edit/tweet/(?P<pk>\d+)$', 'edit_tweet', name='edit_tweet'),   
)
