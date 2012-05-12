from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
    url(r'^$', 'users', name='users'),
        url(r'^add/user/$', 'add_user',name='add_user'),
        url(r'^user/(?P<pk>\d+)$', 'show_user', name='show_user'),
        url(r'^add/tweet/$', 'add_tweet',name='add_tweet'),
        url(r'^edit/user/(?P<pk>\d+)$', 'edit_user', name='edit_user'),   
<<<<<<< HEAD
	url(r'^edit/tweet/(?P<pk>\d+)$', 'edit_tweet', name='edit_tweet'),
	url(r'^user/delete/(?P<pk>\d+)$', 'delete_user', name='delete_user'),   
	url(r'^tweet/delete/(?P<pk>\d+)$', 'delete_tweet', name='delete_tweet'),
	url(r'^follow/(?P<pk>\d+)$', 'show_follow_me', name='show_follow_me'),
)
=======
		url(r'^edit/tweet/(?P<pk>\d+)$', 'edit_tweet', name='edit_tweet'),
		url(r'^user/delete/(?P<pk>\d+)$', 'delete_user', name='delete_user'),   
		url(r'^tweet/delete/(?P<pk>\d+)$', 'delete_tweet', name='delete_tweet'),      
	)
>>>>>>> 49dc3a7b0b0438a0516e3b51374ecd6ec73c98a1
