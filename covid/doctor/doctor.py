from flask import Blueprint, render_template

import covid.adapters.repository as repo
import covid.clinic.services as clinic_services
import covid.doctor.services as doctor_services


doctor_blueprint = Blueprint(
    'doctor_bp', __name__
)


@doctor_blueprint.route('/clinic/<int:clinic_id>/doctors', methods=['GET'])
def doctors_by_clinic(clinic_id):
    clinic = clinic_services.get_clinic(
        clinic_id,
        repo.repo_instance
    )

    if clinic is None:
        return 'Clinic not found', 404

    doctors = doctor_services.get_doctors_by_clinic(
        clinic_id,
        repo.repo_instance
    )

    return render_template(
        'doctor/doctors.html',
        title='Choose a Doctor',
        clinic=clinic,
        doctors=doctors
    )