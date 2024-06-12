from pydantic import BaseModel, Field

from models.tasks import StatusEnum


class TaskBaseSchema(BaseModel):
    id: int
    creator_id: int = Field(exclude=True)
    file_path: str = Field(exclude=True)


class CreateTaskSchema(BaseModel):
    creator_id: int
    file_path: str

class TaskSchema(TaskBaseSchema, CreateTaskSchema):
    status: StatusEnum
    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True
        arbitrary_types_allowed = True