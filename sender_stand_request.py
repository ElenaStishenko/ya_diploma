import requests
import configuration
import data

def post_new_order(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body
                         )


