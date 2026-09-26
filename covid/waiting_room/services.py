from covid.adapters.repository import AbstractRepository
from covid.domain.domain import Patient, ModelException


def get_waiting_room(doctor_id: int, repo: AbstractRepository):
    doctor = repo.get_doctor(doctor_id)

    if doctor is None:
        raise ModelException(f'Doctor {doctor_id} does not exist')

    waiting_room = doctor.waiting_room

    if waiting_room is None:
        raise ModelException(f'Doctor {doctor_id} does not have a waiting room')

    return waiting_room

def get_estimated_waiting_time(waiting_room):
    return (
        waiting_room.number_of_people
        * waiting_room.waiting_time
    )

def join_waiting_room(doctor_id: int, patient: Patient, repo: AbstractRepository):
    waiting_room = get_waiting_room(doctor_id, repo)

    waiting_room.assign_patient(patient)

    return patient


def get_current_queue(doctor_id: int, repo: AbstractRepository):
    waiting_room = get_waiting_room(doctor_id, repo)

    return waiting_room.current_queue


def get_patient_queue_number(patient: Patient):
    return patient.queue_number