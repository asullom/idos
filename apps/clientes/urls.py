from django.conf.urls import patterns, url
from .views import ClienteListView, ClienteCreateView, \
    ClienteUpdateView, ClienteDeleteView

urlpatterns = patterns(
    '',

    url(r'^cliente/delete/(?P<pk>.*)/$',
        ClienteDeleteView.as_view(), name='cliente-delete'),

    url(r'^cliente/update/(?P<pk>.*)/$',
        ClienteUpdateView.as_view(), name='cliente-update'),

    url(r'^cliente/create/$',
        ClienteCreateView.as_view(), name='cliente-crete'),
    url(r'^cliente/index/$',
        ClienteListView.as_view(), name='cliente-index'),


)
