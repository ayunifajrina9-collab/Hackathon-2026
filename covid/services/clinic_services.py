from typing import List

import covid.adapters.repository as repo
from covid.domain.Clinics import Clinics

def get_clinic(clinic_id: int) -> Clinics | None:
    return repo.repo_instance.get_clinic(clinic_id)

def get_clinics() -> List[Clinics]:
    return repo.repo_instance.get_clinics()