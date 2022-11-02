from flask import Blueprint
from flask import request # Ayuda a obtener la informacion de los json o los parametros o los bearing

from controllers.table_controller import TableController

table_blueprints = Blueprint('table_blueprints', __name__)
table_controller = TableController()