from fastapi import APIRouter, HTTPException
from app.database.connection import execute_query
from app.models.schemas import PatientHistory, VisitDetail

router = APIRouter()

@router.get("/patients/{patient_id}/history", response_model= PatientHistory)
def get_patient_history(patient_id: str):
    query = """
    SELECT * FROM emr_patients
    WHERE patient_id = %s
    """
    patients = execute_query(query, (patient_id,))
    if patient is None:
        raise HTTPException(status_code=500, detail="Database error")
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    visit_query = """
    SELECT * FROM emr_visits
    WHERE patient_id = %s
    """
    visits = execute_query(visit_query, (patient_id,))
    if visits is None:
        raise HTTPException(status_code=500, detail="Database error")
    
    visit_details = []
    for visit in visits:
        prescriptions_query = """
        SELECT * FROM emr_prescriptions 
        WHERE visit_id = %s
        """
        prescriptions = execute_query(prescriptions_query, (visit['visit_id'],))

        tests_query = """
        SELECT * FROM emr_tests
        WHERE visit_id = %s
        """
        tests = execute_query(tests_query, (visit['visit_id'],))

        visit_detail = VisitDetail(
            **visit,
            prescriptions=prescriptions or [],
            tests = tests or []
        )
        visit_details.append(visit_detail)
    
    patient_history = PatientHistory(
        **patient[0],
        visits= visit_details
    )
    return patient_history