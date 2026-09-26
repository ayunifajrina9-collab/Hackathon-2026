"""Initialize Flask app."""

from pathlib import Path

from flask import Flask

import covid.adapters.repository as repo
from covid.adapters.loader import MemoryRepository, populate


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = Path('covid') / 'adapters' / 'data'

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    # fill the content of the repository from the provided csv files
    populate(data_path, repo.repo_instance)

    # Build the application - these steps require an application context.
    with app.app_context():
        # Register blueprints.

        from .clinic import clinic
        app.register_blueprint(clinic.clinic_blueprint)

        from .doctor import doctor
        app.register_blueprint(doctor.doctor_blueprint)

        from .waiting_room import waiting_room
        app.register_blueprint(waiting_room.waiting_room_blueprint)

        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

    return app
