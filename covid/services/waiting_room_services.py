import covid.adapters.repository as repo
from covid.domain.Clinics import Patient, ModelException


def join_waiting_room(doctor_id: int, patient: Patient):
    doctor = repo.repo_instance.get_doctor(doctor_id)

    if doctor is None:
        raise ModelException(f'Doctor {doctor_id} does not exist')

    waiting_room = doctor.waiting_room

    if waiting_room is None:
        raise ModelException(f'Doctor {doctor_id} does not have a waiting room')

    waiting_room.assign_patient(patient)

    return patient


def get_waiting_room(doctor_id: int):
    doctor = repo.repo_instance.get_doctor(doctor_id)

    if doctor is None:
        raise ModelException(f'Doctor {doctor_id} does not exist')

    waiting_room = doctor.waiting_room

    if waiting_room is None:
        raise ModelException(f'Doctor {doctor_id} does not have a waiting room')

    return waiting_room


def get_current_queue(doctor_id: int):
    waiting_room = get_waiting_room(doctor_id)

    return waiting_room.current_queue


def get_patient_queue_number(patient: Patient):
    return patient.queue_number