from flask import Blueprint
from flask import request # Ayuda a obtener la informacion de los json o los parametros o los bearing

from controllers.political_party_controller import PoliticalPartyController

political_party_blueprints = Blueprint('political_party_blueprints', __name__)
political_party_controller = PoliticalPartyController()