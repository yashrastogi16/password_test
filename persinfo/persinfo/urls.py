from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'persinfo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'details.views.home', name='home'),
    url(r'^login/$', 'details.views.login', name='login'),
    url(r'^login/user-login/$', 'details.views.user_login', name='user_login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^recover/(?P<signature>.+)/$', 'details.views.recover_done',
        name='password_reset_sent'),
    url(r'^recover/$', 'details.views.recover', name='password_reset_recover'),
    url(r'^reset/done/$', 'details.views.reset_done', name='password_reset_done'),
    url(r'^reset/(?P<token>[\w:-]+)/$', 'details.views.reset',
        name='password_reset_reset'),
    #url(r'^resetpassword/passwordsent/$','django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    #url(r'^resetpassword/$','django.contrib.auth.views.password_reset', name='reset_password_reset1'),
    #url(r'^reset/(?P<uid64>[0-9A-Za-z]+)/(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    #url(r'^reset/done/$','django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    
)
if settings.DEBUG:
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT, }),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, })


