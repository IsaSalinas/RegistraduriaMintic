import json
from flask import Flask, app
from flask import jsonify # coge un dicc y lo pasa a json
from flask_cors import CORS
from waitress import serve

from blueprints.political_party_blueprints import political_party_blueprints
from blueprints.candidate_blueprints import candidate_blueprints
from blueprints.vote_blueprints import vote_blueprints
from blueprints.table_blueprints import table_blueprints

regisApp = Flask(__name__)
cors = CORS(regisApp)

app.register_blueprint(political_party_blueprints)
app.register_blueprint(candidate_blueprints)
app.register_blueprint(vote_blueprints)
app.register_blueprint(table_blueprints)


@regisApp.route("/", methods=['GET']) #anotacion para crear un endpoint
    #Para la respuesta creamos una funcion.
def home():
    response={"message": "Welcome to Registraduria MINTIC"}
    return jsonify(response) #coge el dicc y lo pasa a json, aunque ya no es necesario


#=========Config and Execution code===============
def load_file_config():
    with open("config.json", "r") as config:
        data = json.load(config) #Carga el json de config y lo pasa a un dicc
    return data

     #Variable interna que hace referencia al nombre del proyecto
if __name__ == '__main__':
    data_config = load_file_config() #Guarda lo que retorna la funcion, la version en diccionario del Json
    print("Server running: http://" + data_config.get('url-backend') + ":" + str(data_config.get('port')))
    serve(regisApp, host=data_config.get('url-backend'), port=data_config.get('port'))# permite desplegar la aplicacion
    #Coja esta aplicacion y pongala en esta IP en este puerto.
