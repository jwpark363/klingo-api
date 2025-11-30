## scenario, quest progress state management api
from pydantic import BaseModel
from enum import Enum
from db.model.scenario import StageType
from db.model.progress import ProgressState
from common.evaluation import GradeType

class ProgressInfo(BaseModel):
    user_id: int
    scenario_id: int
    stage_type: StageType       ## READING, LISTENING, WRITING, SPEAKING
    state_type: ProgressState   ## START, DOING, DONE

class ProgressRLInfo(ProgressInfo):
    """
        Reading, Listening Progress Info
    """
    result_time: int        # stage progress time(second)
    wrong_idx: list[int]    # incorrect answer index list
    
class ProgressResult(BaseModel):
    grade: GradeType     # Grade for points
    point: float        # point ( 0 ~ 100)
    top_percent: float  # Grades are in the top few percen