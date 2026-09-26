from typing import List

from covid.adapters.repository import AbstractRepository
from covid.domain.domain import Doctor


def get_doctor(doctor_id: int, repo: AbstractRepository) -> Doctor | None:
    return repo.get_doctor(doctor_id)


def get_doctors(repo: AbstractRepository) -> List[Doctor]:
    return repo.get_doctors()

def get_doctors_by_clinic(clinic_id: int, repo: AbstractRepository) -> List[Doctor]:
    doctors = repo.get_doctors()

    return [
        doctor for doctor in doctors
        if doctor.clinic_id == clinic_id
    ]