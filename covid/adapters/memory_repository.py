import csv
from pathlib import Path


class Clinic:
    def __init__(self, clinic_id, clinic_name, waiting_room, waiting_time_minutes):
        self.clinic_id = clinic_id
        self.clinic_name = clinic_name
        self.waiting_room = waiting_room
        self.waiting_time_minutes = waiting_time_minutes
        self.doctors = []

    def __repr__(self):
        return f"<Clinic {self.clinic_id}: {self.clinic_name}>"


class Doctor:
    def __init__(self, doctor_id, doctor_name, clinic_id):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.clinic_id = clinic_id
        self.clinic = None

    def __repr__(self):
        return f"<Doctor {self.doctor_id}: {self.doctor_name}>"


def make_doctor_clinic_association(doctor, clinic):
    doctor.clinic = clinic
    clinic.doctors.append(doctor)


class MemoryRepository:
    def __init__(self):
        self.__doctors = []
        self.__clinics_index = {}

    def add_clinic(self, clinic):
        self.__clinics_index[clinic.clinic_id] = clinic

    def get_clinic(self, clinic_id):
        return self.__clinics_index.get(clinic_id)

    def get_clinics(self):
        return list(self.__clinics_index.values())