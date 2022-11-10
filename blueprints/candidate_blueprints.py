from flask import Blueprint
from flask import request # Ayuda a obtener la informacion de los json o los parametros o los bearing

from controllers.candidate_controller import CandidateController

candidate_blueprints = Blueprint('candidate_blueprints', __name__)
candidate_controller = CandidateController()