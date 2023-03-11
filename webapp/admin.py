from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from webapp.models import Resource


admin.site.site_title = _('Origin server admin')
admin.site.site_header = _('Origin server administration')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass
