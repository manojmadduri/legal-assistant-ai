from fastapi import APIRouter, Depends, HTTPException
import requests
from ..config import settings

router = APIRouter()

@router.post("/check")
def compliance_check(document: str):
    url = "https://api.deepseek.com/analyze"
    payload = {"text": document, "check": "legal_compliance"}
    headers = {"Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}"}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=400, detail="Compliance check failed")
