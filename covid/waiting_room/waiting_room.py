from flask import Blueprint, render_template, session, url_for, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import covid.adapters.repository as repo
import covid.waiting_room.services as services
import covid.clinic.services as clinic_services

from covid.domain.domain import Patient

waiting_room_blueprint = Blueprint(
    'waiting_room_bp', __name__
)

@waiting_room_blueprint.route(
    '/waiting_room/<int:clinic_id>',
    methods=['GET']
)
def waiting_room(clinic_id):

    clinic = clinic_services.get_clinic(
        clinic_id,
        repo.repo_instance
    )

    if clinic is None:
        return 'Clinic not found', 404

    waiting_room = clinic.waiting_room

    estimated_wait = services.get_estimated_waiting_time(
        waiting_room
    )

    return render_template(
        'waiting_room/waiting_room.html',
        title='Waiting Room',
        clinic=clinic,
        waiting_room=waiting_room,
        estimated_wait=estimated_wait
    )

class JoinQueueForm(FlaskForm):
    patient_name = StringField(
        'Name',
        validators=[DataRequired()]
    )

    submit = SubmitField('Join Queue')

@waiting_room_blueprint.route(
    '/waiting_room/<int:clinic_id>/join',
    methods=['GET', 'POST']
)
def join_waiting_room(clinic_id):

    clinic = clinic_services.get_clinic(
        clinic_id,
        repo.repo_instance
    )

    if clinic is None:
        return 'Clinic not found', 404

    waiting_room = clinic.waiting_room

    form = JoinQueueForm()

    if form.validate_on_submit():

        patient_id = repo.repo_instance.get_next_patient_id()

        patient = Patient(
            patient_id=patient_id,
            patient_name=form.patient_name.data
        )

        repo.repo_instance.add_patient(patient)

        waiting_room.assign_patient(patient)

        session['patient_id'] = patient.patient_id
        session['clinic_id'] = clinic.clinic_id

        return render_template(
            'waiting_room/queue_number.html',
            title='Your Queue Number',
            clinic=clinic,
            patient=patient
        )

    return render_template(
        'waiting_room/join.html',
        title='Join Queue',
        clinic=clinic,
        form=form
    )

@waiting_room_blueprint.route(
    '/waiting_room/<int:clinic_id>/patient',
    methods=['GET']
)
def patient_status(clinic_id):

    clinic = clinic_services.get_clinic(
        clinic_id,
        repo.repo_instance
    )

    if clinic is None:
        return 'Clinic not found', 404

    patient_id = session.get('patient_id')

    if patient_id is None:
        return 'No patient is currently registered', 404

    patient = repo.repo_instance.get_patient(patient_id)

    if patient is None:
        return 'Patient not found', 404

    waiting_room = clinic.waiting_room

    estimated_wait = services.get_estimated_waiting_time(
        waiting_room
    )

    return render_template(
        'waiting_room/patient_status.html',
        title='Your Waiting Status',
        clinic=clinic,
        patient=patient,
        waiting_room=waiting_room,
        estimated_wait=estimated_wait
    )

@waiting_room_blueprint.route('/clear_patient')
def clear_patient():
    session.pop('patient_id', None)
    session.pop('clinic_id', None)

    return redirect(url_for('home_bp.home'))