from sender_stand_request import post_new_order
import configuration
import requests
import data

# Елена Стишенко, 21-я когорта — Финальный проект. Инженер по тестированию плюс


def get_url_with_track(body_order):
    order_track = post_new_order(data.body_order).json()["track"]
    return order_track

def post_url_with_track(body_order):
    post_track_path = get_url_with_track(post_new_order(data.body_order))
    url_track = configuration.GET_ORDER_PATH +"?t=" + str(post_track_path)
    return  url_track


def post_track_order(order):
    post_track = requests.get(configuration.URL_SERVICE + post_url_with_track(order))
    print (post_track)
    assert post_track.status_code == 200


post_track_order(data.body_order)



