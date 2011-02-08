from urlparse import urljoin
from datetime import datetime

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf.urls.defaults import patterns, url
from django.template.loader import render_to_string

from models import Setting, SettingItem

class SettingItemInline(admin.TabularInline):
    model = SettingItem
    extra = 1

class SettingAdmin(admin.ModelAdmin):
    list_display = ('site', 'group')
    inlines = (SettingItemInline,)

admin.site.register(Setting, SettingAdmin)

