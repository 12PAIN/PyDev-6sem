from pydantic import BaseModel, Field
from typing import List


class Part(BaseModel):
    name: str
    pcs: int


class ResultSchema(BaseModel):
    task_id: int
    parts: List[Part]
    input_img_code: str | None
    output_img_code: str | None
