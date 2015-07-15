from django.conf.urls import patterns, include, url
from django.contrib import admin
from RBuser.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'redbrick.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # user part
    url(r'^home/','RBuser.views.home'),
    url(r'^login/','RBuser.views.login'),
    url(r'^register/','RBuser.views.register'),

    # discuss part


    #project part


    #vedio part



    #admin part
    url(r'^admin/', include(admin.site.urls)),
)
