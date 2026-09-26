import csv
from pathlib import Path

from covid.domain.Clinics import Clinics, WaitingRoom, Doctor

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

    def add_doctor(self, doctor):
        self.__doctors.append(doctor)

    def get_doctors(self):
        return self.__doctors


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
            number_of_people=int(data_row[3]),
            status=data_row[4]
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


if __name__ == "__main__":
    repo = MemoryRepository()
    base_path = Path(__file__).parent / "doctorclinic_data"
    populate(base_path, repo)

    print("=== Clinics loaded ===")
    for clinic in repo.get_clinics():
        print(clinic)

    print("\n=== Doctors loaded ===")
    for doctor in repo.get_doctors():
        print(doctor)