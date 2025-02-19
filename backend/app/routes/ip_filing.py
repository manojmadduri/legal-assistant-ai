from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

USPTO_API_URL = "https://developer.uspto.gov/ip-api/"

@router.post("/file-patent")
def file_patent(data: dict):
    try:
        response = requests.post(USPTO_API_URL + "patent", json=data)
        if response.status_code == 201:
            return {"message": "Patent filing successful", "tracking_id": response.json().get('tracking_id')}
        else:
            raise HTTPException(status_code=400, detail="Filing failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
