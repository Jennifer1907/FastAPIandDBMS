from fastapi import APIRouter, HTTPException
from typing import List
from app.database.connection import execute_query
from app.models.schemas import Patient

router = APIRouter()

@router.get("/patients/", response_model=List[Patient])
def get_patients(skip: int=0, limit: int=100):
    query = """
    SELECT * FROM emr_patients
    LIMIT %s OFFSET %s
    """
    patients = execute_query(query, (limit, skip))
    if patients is None:
        raise HTTPException(status_code=500, detail = "Database error")
    return patients

@router.get("/patients/search", response_model = List[Patient])
def search_patients(name: str):
    query = """
    SELECT * FROM emr_patients
    WHERE LOWER(CONCAT(first_name,last_name)) LIKE LOWER(%s)
    """
    search_term = f"%{name}%"
    patients = execute_query(query, (search_term, search_term))
    if patients is None:
        raise HTTPException(status_code=500, detail = "Database error")
    return patients

@router.get("/patients/{patient_id}", response_model = List[Patient])
def get_patient(patient_id: str):
    query = """
    SELECT * FROM emr_patients
    WHERE patient_id = %s
    """
    patients = execute_query(query, (patient_id,))
    if patient is None:
        raise HTTPException(status_code=500, detail="Database error")
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient[0] 