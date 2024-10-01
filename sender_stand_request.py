import requests
import configuration

def post_new_order(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body
                         )


def get_track_order(track):
    return requests.get(configuration.URL_SERVICE + track)