from twitch_client.exceptions import TwitchAuthException

def oauth_required(func):
    def wrapper(*args, **kwargs):

        if not args[0]._oauth_token:
            raise TwitchAuthException('OAuth token required')
        return func(*args, **kwargs)
    return wrapper
