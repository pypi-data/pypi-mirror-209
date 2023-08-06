from fastapi import APIRouter
import os
from core.rule.rule_engine_manager import RuleEngineManager

from models.rule_models import EvaluateRule

router = APIRouter()

@router.post("/rule")
def add_rule():
    return "Ok"

@router.get("/rule/{id}")
def get_rule(id):
    return "Ok"

@router.get("/rules")
def get_rules():
    return "Ok"

@router.delete("/rule")
def delete_rule():
    return "Ok"

@router.post("/rule/evaluate")
def evaluate_rule(rule: EvaluateRule):
     with RuleEngineManager() as rem:
         return rem.evaluate_expression(rule.expression, rule.data)