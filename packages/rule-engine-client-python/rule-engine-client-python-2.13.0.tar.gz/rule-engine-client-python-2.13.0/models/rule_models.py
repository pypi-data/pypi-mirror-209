from pydantic import BaseModel


class EvaluateRule(BaseModel):
    expression: str
    data: dict