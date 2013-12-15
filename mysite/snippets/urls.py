from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from snippets.models import Snippet

urlpatterns = patterns('',
    # url(r'^$',
    #     ListView.as_view(
    #         queryset=Poll.objects.order_by('-pub_date')[:5],
    #         context_object_name='latest_poll_list',
    #         template_name='polls/index.html')),
    # url(r'^(?P<pk>\d+)/$',
    #     DetailView.as_view(
    #         model=Poll,
    #         template_name='polls/detail.html')),
    # url(r'^(?P<pk>\d+)/results/$',
    #     DetailView.as_view(
    #         model=Poll,
    #         template_name='polls/results.html'),
    #     name='poll_results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

    url(r'^$', 'snippets.views.snippet', name='index'),

    url(r'^add/$', 'snippets.views.addsnippet', name='add'),

    url(r'^save/$', 'snippets.views.savesnippet', name='save'),

    url(r'^delete/$', 'snippets.views.deletesnippet', name='delete'),

    url(r'^(?P<pk>\d+)/$',
    DetailView.as_view(
        model=Snippet,
        template_name='snippets/details.html')),
)