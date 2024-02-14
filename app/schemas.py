import enum
from marshmallow import Schema, fields


class CreateTask(Schema):
    task = fields.Str()


class UpdateTask(CreateTask):
    completed = fields.Bool()


class Task(UpdateTask):
    id = fields.UUID()
    created = fields.DateTime()


class ListTasks(Schema):
    tasks = fields.List(fields.Nested(Task))


class SortByEnum(enum.Enum):
    task = "task"
    created = "created"


class SortDirectionEnum(enum.Enum):
    asc = "asc"
    desc = "desc"


class ListTasksParameters(Schema):
    order_by = fields.Enum(SortByEnum, load_default=SortByEnum.created)
    order = fields.Enum(SortDirectionEnum, load_default=SortDirectionEnum.asc)
