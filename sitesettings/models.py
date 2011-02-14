import datetime

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy  as _
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

class Setting(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('Site'), default=setting.SITE_ID)
    group = models.CharField(_('Group'), max_length=20, default="default")

    objects = CurrentSiteManager()

    class Meta:
        verbose_name = _("Setting")
        verbose_name_plural = _("Settings")
        unique_together = ('site', 'group')

    def __getattr__(self, name):
        try:
            return self.items.get(key=name).value
        except:
            raise KeyError

class SettingItem(models.Model):
    setting = models.ForeignKey(Setting, verbose_name=_('Setting'), related_name='items')
    key = models.CharField(_('Key'), max_length=20)
    value = models.CharField(_('Value'), max_length=200)
    in_context = models.BooleanField(_('In context'), default=False)

class SiteSetting(object):
    def __init__(self):
        self.queryset = Setting.objects

    def __getattr__(self, name):
        try:
            return self.queryset.get(group=name)
        except:
            raise KeyError

settings = SiteSetting()