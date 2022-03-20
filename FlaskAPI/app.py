import os
from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask_cors import CORS
import recommendation as rec
from recommendation import Person

# pylint: disable=C0103
app = Flask(__name__)
CORS(app)
cred = credentials.Certificate('vaccine-checklist-837f53fcaf08.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/SetUserData", methods=['POST'])
def SetUserData():

    assert request.method == 'POST'
    assert request.json != None

    doc_ref = db.collection('UserData').document(str(request.json['ID']))
    doc_ref.set(request.json)

    patient = Person(request.json['bday'], request.json['allergies'], request.json['immunocompromised'], request.json['sex'])

    return {"Vaccines" : [
                            patient.HepB(), 
                            patient.RV(), 
                            patient.DTaP(), 
                            patient.HiB(), 
                            patient.PCV(), 
                            patient.IPV(), 
                            patient.MMR(), 
                            patient.Varicella(),
                            patient.HepA(),
                            patient.HPV(),
                            patient.MenACYW()
                        ]}


@app.route('/GetUserData', methods = ['GET'])
def GetUserData():

    assert request.method == 'GET'
    assert request.headers['ID']

    users_ref = db.collection('UserData')
    docs = users_ref.stream()

    for doc in docs:
        if doc.id == request.headers['ID']:
            return doc.to_dict()

    return {"Result" : "No data found"}

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's running!"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
