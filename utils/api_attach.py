import json
import logging

import allure
import requests
from allure_commons.types import AttachmentType


def api_get(url, **kwargs):
    with allure.step("API Request"):
        responce = requests.get(url, **kwargs)
        allure.attach(body=responce.request.method + " " + responce.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(responce.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(responce.request.url)
        logging.info(responce.status_code)
        logging.info(responce.text)
        return responce

def api_post(url, **kwargs):
    with allure.step("API Request"):
        responce = requests.post(url, **kwargs)
        allure.attach(body=responce.request.method + " " + responce.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(responce.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(responce.request.url)
        logging.info(responce.status_code)
        logging.info(responce.text)
        return responce

def api_put(url, **kwargs):
    with allure.step("API Request"):
        responce = requests.put(url, **kwargs)
        allure.attach(body=responce.request.method + " " + responce.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(responce.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(responce.request.url)
        logging.info(responce.status_code)
        logging.info(responce.text)
        return responce
