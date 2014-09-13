from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'unicef.views.home', name='home'),
    url(
        r'^about/$',
        TemplateView.as_view(template_name="unicef/about.html"),
        name='about'
    ),
    url(
        r'^credits/$',
        TemplateView.as_view(template_name="unicef/credits.html"),
        name='credits'
    ),
    url(
        r'^contact/$',
        TemplateView.as_view(template_name="unicef/contact.html"),
        name='contact'
    ),
    url(
        r'^about/the-facts/$',
        TemplateView.as_view(template_name="unicef/the_facts.html"),
        name='about_the_facts'
    ),
    url(
        r'^about/treatment/$',
        TemplateView.as_view(template_name="unicef/treatment.html"),
        name='about_treatment'
    ),
    url(
        r'^about/safe-burial-practices/$',
        TemplateView.as_view(template_name="unicef/safe_burial_practices.html"),
        name='about_safe_burial_practices'
    ),
    url(
        r'^content/(?P<category_slug>[\w-]+)/list/$',
        'unicef.views.ebola_category_object_list',
        {},
        name='category_object_list'
    ),
    #url(r'^search/', cache_page(SearchView(results_per_page=5), 60 * 60), name='haystack_search'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
