from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Doctor(db.Model):
     
     __tablename__ = 'doctors'

     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String)

     patients = db.relationship('Patient', backref='doctors')

class Patient(db.Model):
     
     __tablename__ = 'patients'

     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String)
     doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))

