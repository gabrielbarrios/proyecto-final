from django.conf.urls.defaults import *
urlpatterns = patterns('main.views',
    url(r'^$', 'users', name='users'),
        url(r'^add/user/$', 'add_user',name='add_user'),
        url(r'^add/tweet/$', 'add_tweet',name='add_tweet'),
)
