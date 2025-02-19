from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import base, models
from ..schemas import schemas

router = APIRouter()

@router.post("/create", response_model=schemas.DocumentResponse)
def create_document(doc: schemas.DocumentCreate, db: Session = Depends(base.SessionLocal)):
    new_doc = models.Document(title=doc.title, content=doc.content, owner_id=1)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

@router.get("/{doc_id}", response_model=schemas.DocumentResponse)
def get_document(doc_id: int, db: Session = Depends(base.SessionLocal)):
    doc = db.query(models.Document).filter(models.Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc
