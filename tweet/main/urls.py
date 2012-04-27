from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'main.views.users', name='user'),
        url(r'^add/user/$', 'main.views.add_user',name='add_user'),
        url(r'^add/tweet/$', 'main.views.add_tweet',name='add_tweet'),
)
