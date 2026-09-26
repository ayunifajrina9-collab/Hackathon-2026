import csv
from pathlib import Path

from covid.domain.domain import Clinics, WaitingRoom, Doctor

class MemoryRepository:
    def __init__(self):
        self.__doctors = []
        self.__clinics_index = {}
        self.__patients = []
        self.__next_patient_id = 1

    def add_clinic(self, clinic):
        self.__clinics_index[clinic.clinic_id] = clinic

    def get_clinic(self, clinic_id):
        return self.__clinics_index.get(clinic_id)

    def get_clinics(self):
        return list(self.__clinics_index.values())

    def add_doctor(self, doctor):
        self.__doctors.append(doctor)

    def get_doctors(self):
        return self.__doctors

    def get_doctor(self, doctor_id):
        for doctor in self.__doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_patients(self):
        return list(self.__patients)

    def get_patient(self, patient_id):
        for patient in self.__patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def get_next_patient_id(self):
        patient_id = self.__next_patient_id
        self.__next_patient_id += 1
        return patient_id


def read_csv_file(filename):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        for row in reader:
            row = [item.strip() for item in row]
            if row:
                yield row


def load_clinics(base_path, repo):
    clinics_filename = str(base_path / "clinic" / "clinic.csv")

    for data_row in read_csv_file(clinics_filename):
        clinic = Clinics(
            clinic_id=int(data_row[0]),
            clinic_name=data_row[1]
        )

        waiting_room = WaitingRoom(
            waiting_time=int(data_row[2]),
        )

        clinic.add_waiting_room(waiting_room)

        repo.add_clinic(clinic)


def load_doctors(base_path, repo):
    doctors_filename = str(base_path / "doctor" / "Book(doctor).csv")

    for data_row in read_csv_file(doctors_filename):
        doctor = Doctor(
            doctor_id=int(data_row[0]),
            doctor_name=data_row[1],
            clinic_id=int(data_row[2])
        )

        clinic = repo.get_clinic(doctor.clinic_id)

        if clinic is not None:
            doctor.set_waiting_room(clinic.waiting_room)

        repo.add_doctor(doctor)

def populate(base_path, repo):
    load_clinics(base_path, repo)
    load_doctors(base_path, repo)
