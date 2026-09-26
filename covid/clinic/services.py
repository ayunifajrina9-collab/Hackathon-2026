from typing import List

from covid.adapters.repository import AbstractRepository
from covid.domain.domain import Clinics


def get_clinic(clinic_id: int, repo: AbstractRepository) -> Clinics | None:
    return repo.get_clinic(clinic_id)


def get_clinics(repo: AbstractRepository) -> List[Clinics]:
    return repo.get_clinics()