from faker import Faker
from random import choice as rc
import random
import ipdb

from app import app
from models import db, Doctor, Patient


# db.init_app(app)

fake = Faker()

with app.app_context():
    Doctor.query.delete()
    Patient.query.delete()

    doctors = []
    for n in range(30):
        doctor = Doctor(name = fake.name())
        doctors.append(doctor)
    db.session.add_all(doctors)

    patients = []
    for i in range(60):
        # patien = Pet(name=fake.first_name(), species=rc(species), owner=rc(owners))
        patient = Patient(name = fake.name(), doctor_id = random.randint(0,60))
        patients.append(patient)

    db.session.add_all(patients)
    db.session.commit()
    print("DONE")

    mypat = Patient.query.first()
    ipdb.set_trace()