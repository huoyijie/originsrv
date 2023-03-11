from django.utils.translation import gettext, gettext_lazy as _
from django.db import models


class Resource(models.Model):
    file = models.FileField(verbose_name=_('File'), upload_to='uploads/%Y/%m/')

    def __str__(self):
        return gettext('File')

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')
