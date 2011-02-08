from django.conf import settings
from django.contrib.sites.models import Site

from models import Setting

def settings(request):
    context = {}

    for setting in Setting.objects.all():
        context_item = {}

        for item in setting.items.filter(in_context=True).all():
            context_item[item.key] = item.value

        if context_item:
            context[setting.group] = context_item

    return context