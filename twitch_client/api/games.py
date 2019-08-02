from twitch_client.api.base import TwitchAPI
from twitch_client.exceptions import TwitchAttributeException
from twitch_client.resources import TopGame


class Games(TwitchAPI):

    def get_top(self, limit=10, offset=0):
        if limit > 100:
            raise TwitchAttributeException(
                'Maximum number of objects returned in one request is 100')

        params = {
            'limit': limit,
            'offset': offset
        }
        response = self._request_get('games/top', params=params)
        return [TopGame.construct_from(x) for x in response['top']]
