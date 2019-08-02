import logging
from django.contrib.sites.models import Site
from django.utils.http import urlencode

from twitch_auth import app_settings
logger = logging.getLogger(__name__)

def get_absolute_uri(url):
    return app_settings.PROTOCOL+app_settings.REDIRECT_URI
    # return app_settings.PROTOCOL + "%s%s" % (Site.objects.get_current().domain, url)

def build_url2(url, extra_params):
    params = {
        'client_id': app_settings.CLIENT_ID,
    }
    params.update(extra_params)
    return "%s?%s" % (url, urlencode(params))

def build_url(url, extra_params):
    params = {
        'client_id': app_settings.CLIENT_ID,
        'response_type': 'code'
    }
    params.update(extra_params)
    url2 = "%s?%s" % (url, urlencode(params)) + "&scope="+app_settings.SCOPE
    # logger.error("%s?%s" % (url, params))
    return url2
