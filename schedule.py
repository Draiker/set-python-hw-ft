import json
import requests
from urllib import parse
from re import match
from datetime import datetime
import logging
import sys


class Schedule:
    
    logging.basicConfig(stream=sys.stdout, level="DEBUG")
    _queueList = []
    _api_url = None
    _api_endpoint = None

    _HTTP_TIMEOUT = 30000

    _buffer = {}
    _headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=utf-8'
    }

    def __init__(self, api_url, api_endpoint, queueList):
        try:
            self._api_url = str(api_url)
            self._api_endpoint = str(api_endpoint)
            self._queueList = queueList

        except TypeError as err:
            print("Wrong parameter type", err)
        
    def getScheduleFull(self):
        
        fullSchedule = []
        try:
            for queue in self._queueList:
                data = {
                    "queue": queue
                }
                logging.info(data)

                response = requests.post(
                    self._api_url + self._api_endpoint,
                    json=data,
                    headers=self._headers,
                    timeout=self._HTTP_TIMEOUT
                )

                if response.json():
                    response_body = response.json()
                    if response.status_code < 300:
                        fullSchedule.append(response_body)
                        logging.info(str(response))
                        # logging.info(str(response_body))
                    else:
                        logging.warning(response_body)
                        raise Exception('Wrong queue name: ' + str(response.status_code) + " " + str(response.content))
        except Exception as err:
            print(err.with_traceback)
        return fullSchedule