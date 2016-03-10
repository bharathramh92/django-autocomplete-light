from django import forms
from possiblebug.models import Author, Publisher
from dal import autocomplete


class NewBookAuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['test', ]
        widgets = {
            'test': autocomplete.ModelSelect2Multiple(url='possiblebug:author-autocomplete')
        }
        labels = {
            'test': "Authors",
        }


class NewBookPublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = ['test', ]
        widgets = {
            'test': autocomplete.ModelSelect2(url='possiblebug:publisher-autocomplete')
        }
        labels = {
            'test': "Publisher",
        }