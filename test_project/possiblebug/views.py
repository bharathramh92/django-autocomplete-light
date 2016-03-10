from django.shortcuts import render
from dal import autocomplete
from possiblebug.models import Author, Publisher
from possiblebug.forms import NewBookAuthorForm, NewBookPublisherForm
# Create your views here.


class AuthorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        qs = Author.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class PublisherAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        qs = Publisher.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


def add_new_book(request):
    forms = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        authorForm = NewBookAuthorForm(request.POST)
        publisherForm = NewBookPublisherForm(request.POST)

        forms['authorForm'] = authorForm
        forms['publisherForm'] = publisherForm

        # check whether it's valid:
        if authorForm.is_valid() and publisherForm.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            publisher = publisherForm.cleaned_data['name']
            authors = authorForm.cleaned_data['name']
            print("Publisher ", publisher)
            print("Authors ", authors)

        print("A", authorForm.errors)
        print("p", publisherForm.errors)
    # if a GET (or any other method) we'll create a blank form
    else:

        forms['authorForm'] = NewBookAuthorForm()
        forms['publisherForm'] = NewBookPublisherForm()
    return render(request, "possiblebug/test.html", forms)
