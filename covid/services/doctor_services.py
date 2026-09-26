from typing import List

import covid.adapters.repository as repo
from covid.domain.Clinics import Doctor

def get_doctor(doctor_id: int) -> Doctor | None:
    return repo.repo_instance.get_doctor(doctor_id)

def get_doctors() -> List[Doctor]:
    return repo.repo_instance.get_doctors()