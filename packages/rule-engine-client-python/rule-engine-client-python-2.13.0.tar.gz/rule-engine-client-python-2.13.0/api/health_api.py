from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/health")
def health():
    return "Ok"