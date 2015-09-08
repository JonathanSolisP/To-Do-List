__author__ = 'Proyecto'

from base.base_test import BaseTest
from configs.base_framework_configs import GlobalConfigs as GC


class TestTaskRequests(BaseTest):

    def test_get_all_tasks(self):
        response = self.test_management.get_all_tasks()
        assert response.status_code == 200, GC.ERROR_GET_ALL_TASK

    def test_get_task_by_id(self):
        self.task_id = 5

        response = self.test_management.get_task_by_id(self.task_id)
        assert response.status_code == 200, GC.ERROR_GET_TASK_BY_ID

    def test_post_task(self):
        self.payload = {"content": [{"name": "Roger", "description": "Install"}]}

        self.payload = GC.encode_dictionary(self.payload)
        response = self.test_management.post_tasks(self.payload)
        assert response.status_code == 200, GC.ERROR_POST_TASKS

    def test_post_tasks(self):
        self.payload = {"content": [{"name": "Leonardo", "description": "Repair"},
                                    {"name": "Francisco", "description": "Fix"}]}

        self.payload = GC.encode_dictionary(self.payload)
        response = self.test_management.post_tasks(self.payload)
        assert response.status_code == 200, GC.ERROR_POST_TASKS

    def test_update_task(self):
        self.task_id = 5
        self.payload = {"content": {"name": "NAME_UPDATE_TEST", "description": "DESCRIPTION_UPDATE_TEST"},
                        "id": self.task_id}

        self.payload = GC.encode_dictionary(self.payload)
        response = self.test_management.put_task(self.payload)
        assert response.status_code == 200, GC.ERROR_UPDATE_TASK

    def test_delete_task(self):
        self.task_id = 6
        self.payload = {"id": self.task_id}

        self.payload = GC.encode_dictionary(self.payload)
        response = self.test_management.delete_task(self.payload)
        assert response.status_code == 200, GC.ERROR_DELETE_TASK










