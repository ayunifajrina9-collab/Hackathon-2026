class Clinics:
    def __init__(self, clinic_id: int, clinic_name: str):
        self.__clinic_id: int = clinic_id
        self.__clinic_name: str = clinic_name
        self.__waiting_room: WaitingRoom = None

    @property
    def clinic_id(self) -> int:
        return self.__clinic_id

    @property
    def clinic_name(self) -> str:
        return self.__clinic_name

    @property
    def waiting_room(self) -> 'WaitingRoom':
        return self.__waiting_room

    def add_waiting_room(self, waiting_room: 'WaitingRoom'):
        self.__waiting_room = waiting_room

    def __repr__(self) -> str:
        return f'<Clinics {self.__clinic_id} {self.__clinic_name}>'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Clinics):
            return False
        return other.clinic_id == self.clinic_id
class WaitingRoom:
    def __init__(self, waiting_time: int, number_of_people: int, status: str):
        self.__waiting_time: int = waiting_time
        self.__number_of_people: int = number_of_people
        self.__status: str = status

    @property
    def waiting_time(self) -> int:
        return self.__waiting_time

    @property
    def number_of_people(self) -> int:
        return self.__number_of_people

    @property
    def status(self) -> str:
        return self.__status

    def __repr__(self) -> str:
        return (
            f'<WaitingRoom '
            f'waiting_time={self.__waiting_time} '
            f'number_of_people={self.__number_of_people} '
            f'status={self.__status}>'
        )

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

    def queue_number(self) -> int:
        return self.__queue_number

    @queue_number.setter
    def queue_number(self, queue_number: int):
        self.__queue_number = queue_number

    def __repr__(self) -> str:
        return f'<Patient {self.__patient_name} Queue #{self.__queue_number}>'

