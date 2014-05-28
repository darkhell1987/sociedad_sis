from django.conf.urls import patterns, include, url
from sociedad.apps.blog.views import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sociedad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^archivos/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^noticias/$',noticias),
    url(r'^biblioteca/$',biblioteca),
    url(r'^blog/$',blog),
    url(r'^acercade/$',acercade),
    url(r'^privado/$',privado),    
    url(r'^registro/$',registro),
    url(r'^perfil/$',perfil),
    url(r'^privado/$','sociedad.apps.blog.views.index'), 
    url(r'^cerrar/$', 'sociedad.apps.blog.views.cerrar'),
    url(r'^entrada/(?P<pk>\d+)/$','sociedad.apps.blog.views.Entrada'),
    #(r"^month/(\d+)/(\d+)/$","sociedad.apps.blog.views.month"),
    url(r"^poncomentario/(\d+)/$","sociedad.apps.blog.views.poncomentario"),

   # url(r'^ingresar/$','sociedad.apps.blog.views.ingresar'),

)