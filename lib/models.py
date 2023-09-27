from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Doctor(db.Model, SerializerMixin):
     
     __tablename__ = 'doctors'

     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String)

     patients = db.relationship('Patient', backref='doctors')

     serialize_rules = ('-patients.doctors',)

class Patient(db.Model, SerializerMixin):
     
     __tablename__ = 'patients'

     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String)
     doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))

     serialize_rules = ('-doctors.patient',)

