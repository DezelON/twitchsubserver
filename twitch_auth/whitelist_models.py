from django.db import models
from django.utils.translation import ugettext_lazy as _

class DBWhitelist(models.Model):
    nickname = models.TextField(verbose_name=_('nickname'),help_text=_('Nickname in whitelist'))
    old_nickname = models.TextField(verbose_name=_('nickname'),help_text=_('OLD Nickname in whitelist'))
    user_id = models.TextField(verbose_name=_('user_id'),help_text=_('USER ID in default db'))
    sub_twitch = models.TextField(verbose_name=_('sub_twitch'),help_text=_('User is subscriber?'))
    in_whitelist = models.TextField(verbose_name=_('sub_twitch'),help_text=_('User in whitelist on server?'))

    def __str__(self):
        return self.nickname