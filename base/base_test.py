__author__ = 'Proyecto'

from unittest import TestCase
from todolist_requests.tasks_management import TasksManagement


class BaseTest(TestCase):
    def setUp(self):
        self.test_management = TasksManagement()
        self.task_id = 0
        self.payload = dict()

    def tearDown(self):
        self.test_management = None
