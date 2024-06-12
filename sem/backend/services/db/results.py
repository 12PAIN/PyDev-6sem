from sqlalchemy.orm import Session

from models.results import Result
from models.parts import Part
from models.results_parts_rel import ResultsPartsRel
from services.db.parts import get_part_by_name

def get_result_by_task_id(session: Session, task_id: int):

    return session.query(Result).filter(Result.task_id == task_id).first()


def create_result(session: Session, task_id: int, file_in: str, out: str):
    result = Result(task_id=task_id, input_file=file_in, output_file=out)
    session.add(result)
    session.commit()
    session.refresh(result)
    return result


def add_parts_to_result(session: Session, result: Result, part_name: str, pcs: int):

    part = get_part_by_name(session, part_name)

    result_rel = ResultsPartsRel(result_id=result.id, part_id=part.id, pcs=pcs)
    session.add(result_rel)
    session.commit()
    session.refresh(result_rel)
    return result_rel
