from flask_smorest import Blueprint, abort
from flask.views import MethodView

from app.models.tasks import TaskList
from app.schemas import ListTasksParameters, ListTasks, CreateTask, UpdateTask, Task

todo = Blueprint("todo", "todo", url_prefix="/todo", description="TODO API")
task_list = TaskList()


@todo.route("/tasks")
class TodoCollection(MethodView):

    @todo.arguments(ListTasksParameters, location="query")
    @todo.response(status_code=200, schema=ListTasks)
    def get(self, parameters):
        return task_list.get_tasks()

    @todo.arguments(CreateTask)
    @todo.response(status_code=201, schema=Task)
    def post(self, task):
        return task_list.save_task(task)


@todo.route("/tasks/<string:task_id>")
class TodoTask(MethodView):

    @todo.response(status_code=200, schema=Task)
    def get(self, task_id):
        try:
            return task_list.get_by_id(task_id)
        except IndexError:
            abort(404, message=f"Task with id {task_id} not found")

    @todo.arguments(UpdateTask)
    @todo.response(status_code=200, schema=Task)
    def put(self, payload, task_id):
        try:
            updated_task = task_list.update_task(task_id, payload)
            return updated_task
        except IndexError:
            abort(404, message=f"Task with id {task_id} not found")

    @todo.response(status_code=204)
    def delete(self, task_id):
        try:
            return task_list.delete_task(task_id)
        except IndexError:
            abort(404, message=f"Task with id {task_id} not found")
