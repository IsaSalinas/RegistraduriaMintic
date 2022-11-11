from flask import Blueprint
from flask import request

from controllers.vote_controller import VoteController

vote_blueprints = Blueprint('vote_blueprints', __name__)
vote_controller = VoteController()


@vote_blueprints.route("/vote/all", methods=['GET'])
def get_all_vote():
    response = vote_controller.index()
    return response, 200


@vote_blueprints.route("/vote/<string:id_>", methods=['GET'])
def get_vote_by_id(id_):
    response = vote_controller.show(id_)
    return response, 200


@vote_blueprints.route("/vote/candidate/<string:candidate_id>", methods=['GET'])
def get_vote_by_candidate(candidate_id):
    response = vote_controller.get_by_candidate(candidate_id)
    return response, 200

@vote_blueprints.route("/vote/political_party/<string:political_party_id>", methods=['GET'])
def get_vote_by_political_party(political_party_id):
    response = vote_controller.get_by_political_party(political_party_id)
    return response, 200

@vote_blueprints.route("/vote/table/<string:table_id>", methods=['GET'])
def get_vote_by_table(table_id):
    response = vote_controller.get_by_table(table_id)
    return response, 200

@vote_blueprints.route("/vote/insert/candidate/<string:candidate_id>/table/<string:table_id>", methods=['POST'])
def insert_vote(candidate_id, table_id):
    vote = request.get_json()
    response = vote_controller.create(vote, candidate_id, table_id)
    return response, 201


@vote_blueprints.route("/vote/update/<string:id_>", methods=['PACTH'])
def update_vote(id_):
    vote = request.get_json()
    response = vote_controller.update(id_, vote)
    return response, 201


@vote_blueprints.route("/vote/delete/<string:id_>", methods=['DELETE'])
def delete_vote(id_):
    response = vote_controller.delete(id_)
    return response, 204
