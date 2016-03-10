from django.conf.urls import  url
from possiblebug.views import PublisherAutocomplete, AuthorAutocomplete
from possiblebug import views

urlpatterns = [


    url(
        r'^author-autocomplete/$',
        AuthorAutocomplete.as_view(),
        name='author-autocomplete',
    ),
    url(
        r'^publisher-autocomplete/$',
        PublisherAutocomplete.as_view(),
        name='publisher-autocomplete',
    ),

    url(r'^test/$', views.add_new_book, name="test"),

]