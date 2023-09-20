from flask import Flask, make_response, jsonify 
from flask_migrate import Migrate
from models import db, Patient

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapp.db'

migrate = Migrate(app, db)
db.init_app(app)

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








if __name__ == '__main__':
    app.run()