from flask import Flask, make_response, jsonify 
from flask_migrate import Migrate
from models import db, Patient, Doctor
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapp.db'

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

@app.route('/', methods=['GET','POST'])
def home():
    return '<h1>Hello there</h1>'

@app.route('/patients/<int:id>')
def getpatient(id):
    ourpatient = Patient.query.filter_by(id=id).first()
    # print(ourpatient)
    patientobj = {"patient-name":ourpatient.name, "doctor":ourpatient.doctors.name}
    resp = make_response(jsonify(patientobj), 200)
    return resp

class DoctorsRoutes(Resource):
    def get(self):
        doctorslist = []
        all_doctors = Doctor.query.all()
        for i in all_doctors:
            docObj = i.to_dict()
            doctorslist.append(docObj)
        response = make_response(jsonify(doctorslist), 200)
        return response
    
    # def post(self):

        

        # return '<h1>Uko kwa Doctors</h1>'
api.add_resource(DoctorsRoutes,'/doctors')  #localhost/doctors localhost/doctor/id









if __name__ == '__main__':
    app.run()