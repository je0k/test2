from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'methods.views.home', name='home'),
    # url(r'^methods/', include('methods.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^check-get.html$', 'methods.views.checkGet', name='check-get'),
    url(r'^check-post.html$', 'methods.views.checkPost', name='check-post'),
    url(r'^index.html$', 'methods.views.index', name='index'),
    url(r'^$', 'methods.views.index', name='index'),
)
