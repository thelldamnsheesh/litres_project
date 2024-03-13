import json
import logging
import allure
import requests
from allure_commons.types import AttachmentType


def request(url, method, **kwargs):
    with allure.step("API Request"):
        if method == 'PUT':
            response = requests.put(url, **kwargs)
        if method == 'GET':
            response = requests.get(url, **kwargs)
        if method == 'POST':
            response = requests.post(url, **kwargs)
        allure.attach(body=response.request.method + " " + response.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        if response.text == '':
            allure.attach(body='Ответ пустой', name="Response")
            logging.info(response.request.url)
            logging.info(response.status_code)
            logging.info(response.text)
            return response
        else:
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                          attachment_type=AttachmentType.JSON, extension="json")

            logging.info(response.request.url)
            logging.info(response.status_code)
            logging.info(response.text)
            return response
