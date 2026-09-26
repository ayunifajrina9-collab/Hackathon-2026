from datetime import date, datetime
from typing import List, Iterable


class WaitingRoom:
    pass


class Doctor:
    def __init__(self, doctor_id: int, doctor_name: str, clinic_id: int, waiting_room = WaitingRoom):
        self.__id: int = doctor_id
        self.__name: str = doctor_name
        self.__clinic_id: int = clinic_id
        self.__waiting_room: WaitingRoom = waiting_room

    @property
    def doctor_id(self) -> int:
        return self.__id

    @property
    def doctor_name(self) -> str:
        return self.__name

    @property
    def clinic_id(self) -> int:
        return self.__clinic_id

    @property
    def waiting_room(self) -> WaitingRoom:
        return self.__waiting_room

    def set_waiting_room(self, waiting_room: 'WaitingRoom'):
        self.__waiting_room = waiting_room

    def __repr__(self):
        return f'<Doctor {self.doctor_id} {self.doctor_name}>'

    def __eq__(self, other):
        if not isinstance(other, Doctor):
            return False
        return other.doctor_id == self.doctor_id

class Patient:
    def __init__(self, patient_id: int, patient_name: str):
        self.__id: int = patient_id
        self.__name: str = patient_name

    @property
    def patient_id(self) -> int:
        return self.__id

    @property
    def patient_name(self) -> str:
        return self.__name

    def __repr__(self):
        return f'<Patient {self.patient_id} {self.patient_name}>'

    def __eq__(self, other):
        if not isinstance(other, Patient):
            return False
        return other.patient_id == self.patient_id