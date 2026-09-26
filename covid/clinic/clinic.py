from flask import Blueprint, render_template

import covid.adapters.repository as repo
import covid.clinic.services as services


clinic_blueprint = Blueprint(
    'clinic_bp', __name__
)


@clinic_blueprint.route('/clinics', methods=['GET'])
def clinics():
    clinics = services.get_clinics(repo.repo_instance)

    return render_template(
        'clinic/clinics.html',
        title='Clinics',
        clinics=clinics
    )
