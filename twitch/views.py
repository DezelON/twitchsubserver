import requests
import json
import logging
from django.shortcuts import render
from django.http import HttpResponseRedirect
from twitch_auth import app_settings

from twitch_client import TwitchClient

from twitch_auth.utils import build_url2
from twitch_auth.models import OAuth2AccessToken, TwitchAccount
from twitch_auth.whitelist_models import DBWhitelist
from twitch_auth.backends import OAuth2Backend
from twitch_auth.form import UserLoginForm

logger = logging.getLogger(__name__)

def login(request):
    s = request.session
    if s.get('state')!=None:
        client = TwitchClient(app_settings.CLIENT_ID, OAuth2AccessToken.objects.get(account_id=s.get("_auth_user_id")))
        user = TwitchAccount.objects.get(user_id=s.get("_auth_user_id"))
        logo = user.get_avatar_url()
        name = user.get_name()
        logger.error(s.get("_auth_user_id"))
        if (str(name).lower()=="dezelon".lower() or str(name).lower()=="grandleon".lower()): #grandleon
            data = {
                'status': 200,
                'role': 'author',
                'logo': logo,
                'name': name,
            }
        else:
            data = client.users.check_subscribed_to_channel(user.uid, "grandleon")
            data['role'] = 'user'
            data['logo'] = logo
            data['name'] = name
    else:
        data = {
            'status': 'login',
            'role': 'user',
        }

    if data['status'] == 200:
        data['form'] = UserLoginForm(request.POST or None)
        logger.error(data['form'])
        if request.method == 'POST' and data['form'].is_valid():
            # old_nickname = data['form'].cleaned_data.get('old_nickname', None)
            nickname = data['form'].cleaned_data.get('nickname', None)
            try:
                whitelist_obj = DBWhitelist.objects.using('db_whitelist').get(user_id = s.get("_auth_user_id"))
                whitelist_obj.old_nickname = whitelist_obj.nickname
            except DBWhitelist.DoesNotExist:
                logger.error("2 " + s.get("_auth_user_id"))
                whitelist_obj = DBWhitelist()
                whitelist_obj.user_id = s.get("_auth_user_id")
                whitelist_obj.old_nickname = None
            whitelist_obj.sub_twitch = True
            whitelist_obj.nickname = nickname
            whitelist_obj.in_whitelist = False
            whitelist_obj.save(using='db_whitelist')

    return render(request, "login/index.html", locals())
