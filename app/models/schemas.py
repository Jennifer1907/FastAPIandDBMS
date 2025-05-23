from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Patient(BaseModel):
    patient_id: str
    medical_id: str
    first_name: str
    last_name: str
    date_of_birth: datetime
    gender: str
    address: str
    phone_number: str
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Visit(BaseModel):
    visit_id: str
    patient_id: str
    doctor_id: str
    visit_date: datetime
    symptoms: Optional[str] = None
    diagnosis: Optional[str] = None
    notes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Prescription(BaseModel):
    prescription_id: str
    visit_id: str
    medication_name: str
    dosage: str
    frequency: str
    duration: str
    notes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Test(BaseModel):
    test_id: str
    visit_id: str
    test_name: str
    test_date: datetime
    results: str
    notes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class VisitDetail(Visit):
    prescriptions: List[Prescription] = []
    tests: List[Test] = []

class PatientHistory(Patient):
    visits: List[VisitDetail] = [] 

class VisitOut(Visit):
    visit_id: str