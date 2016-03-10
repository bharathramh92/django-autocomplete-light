from django.contrib import admin
from possiblebug.models import Author, Publisher
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'website', ]}),
    ]
    list_display = ('name', )

admin.site.register(Author, AuthorAdmin)


class PublisherAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'website', 'contact_email']}),
    ]
    list_display = ('name', )

admin.site.register(Publisher, PublisherAdmin)