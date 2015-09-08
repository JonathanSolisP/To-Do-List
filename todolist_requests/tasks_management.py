
from configs.base_framework_configs import GlobalConfigs


class TasksManagement:

    def __init__(self):
        # initialize the session for the requests
        self.GC = GlobalConfigs()
        self.session = GlobalConfigs().create_session()

    def get_all_tasks(self):
        # fetch information of all tasks from database
        url = "{}{}".format(self.GC.URL, self.GC.GET_ALL_EXTENSION)
        response = self.session.get(url)
        return response

    def get_task_by_id(self, task_id):
        # fetch information of a task based on an id
        url = "{}{}".format(self.GC.URL, self.GC.GET_BY_ID_EXTENSION).format(task_id)
        response = self.session.get(url)
        return response

    def post_tasks(self, payload):
        # inserts new tasks in database
        response = self.session.post(self.GC.URL, data=payload, headers=self.GC.HEADERS)
        return response

    def put_task(self, payload):
        # updates information of a task
        response = self.session.put(self.GC.URL, data=payload, headers=self.GC.HEADERS)
        return response

    def delete_task(self, payload):
        # deletes a task from database
        response = self.session.delete(self.GC.URL, data=payload, headers=self.GC.HEADERS)
        return response


