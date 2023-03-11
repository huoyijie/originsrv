from django.utils.translation import gettext_lazy as _
from django.db import models


class Resource(models.Model):
    dir = models.CharField(verbose_name=_(
        'Dir'), max_length=200)
    name = models.CharField(verbose_name=_(
        'Name'), max_length=200, unique=True)
    file = models.FileField(verbose_name=_(
        'File'), upload_to='uploads/%Y/%m/')

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')
