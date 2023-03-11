from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class WebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webapp'
    verbose_name = _('Origin server administration')
