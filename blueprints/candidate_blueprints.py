from flask import Blueprint
from flask import request # Ayuda a obtener la informacion de los json o los parametros o los bearing

from controllers.candidate_controller import CandidateController

candidate_blueprints = Blueprint('candidate_blueprints', __name__)
candidate_controller = CandidateController()


@candidate_blueprints.route("/candidate/all", methods=['GET'])
def get_all_candidate():
    response = candidate_controller.index()
    return response, 200


@candidate_blueprints.route("/candidate/<string:id_>", methods=['GET'])
def get_candidate_by_id(id_):
    response = candidate_controller.show(id_)
    return response, 200


@candidate_blueprints.route("/candidate/insert", methods=['POST'])
def insert_candidate():
    candidate = request.get_json()
    response = candidate_controller.create(candidate)
    return response, 201


@candidate_blueprints.route("/candidate/update/<string:id_>", methods=['PATCH'])
def update_candidate(id_):
    candidate = request.get_json()
    response = candidate_controller.update(id_, candidate)
    return response, 201


@candidate_blueprints.route("/candidate/<string:candidate_id>/political_party/<string:political_party_id>", methods=['PUT'])
def assign_department(candidate_id, political_party_id):
    response = candidate_controller.political_party_assign(candidate_id, political_party_id)
    return response, 201


@candidate_blueprints.route("/candidate/delete/<string:id_>", methods=['DELETE'])
def delete_candidate(id_):
    response = candidate_controller.delete(id_)
    return response, 204
