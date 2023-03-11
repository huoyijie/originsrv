from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from webapp.models import Resource


# class Site(admin.AdminSite):
#     site_title = _('Origin server admin')

#     # Text to put in each page's <h1>.
#     site_header = _('Origin server administration')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass
