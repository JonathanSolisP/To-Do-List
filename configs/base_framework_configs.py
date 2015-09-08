__author__ = 'Solis'
import requests
import json


class GlobalConfigs:

    HTTP_SCHEMA = "http://"
    BASE_URL = "127.0.0.1:8000/Web2pyApp/default/api/"
    GET_ALL_EXTENSION = "tasks.json"
    GET_BY_ID_EXTENSION = "tasks/id/{}.json"

    URL = "{}{}".format(HTTP_SCHEMA, BASE_URL)

    HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    ERROR_GET_ALL_TASK = "Tasks were NOT found"
    ERROR_GET_TASK_BY_ID = "Task was NOT found by id"
    ERROR_POST_TASKS = "Tasks were NOT inserted"
    ERROR_UPDATE_TASK = "Task was NOT updated"
    ERROR_DELETE_TASK = "Task was NOT deleted"

    def __init__(self):
        pass

    @staticmethod
    def create_session():
        return requests.Session()

    @staticmethod
    def encode_dictionary(dictionary):
        return json.dumps(dictionary)



