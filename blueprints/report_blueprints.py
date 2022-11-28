from flask import Blueprint
from controllers.report_controller import ReportController

report_blueprints = Blueprint('report_blueprints', __name__)
report_controller = ReportController()


@report_blueprints.route("/reports/votes_by_total_candidates", methods=['GET'])
def get_votes_by_total_candidates():
    response = report_controller.get_votes_by_total_candidates()
    return response, 200


@report_blueprints.route("/reports/votes_by_candidate", methods=['GET'])
def get_votes_by_candidate():
    response = report_controller.get_votes_by_candidate()
    return response, 200


@report_blueprints.route("/reports/votes_by_total_tables", methods=['GET'])
def get_votes_by_total_tables():
    response = report_controller.get_votes_by_total_tables()
    return response, 200


@report_blueprints.route("/reports/votes_by_table", methods=['GET'])
def get_votes_by_table():
    response = report_controller.get_votes_by_table()
    return response, 200


@report_blueprints.route("/reports/votes_by_political_party", methods=['GET'])
def get_votes_by_political_party():
    response = report_controller.get_votes_by_political_party()
    return response, 200


@report_blueprints.route("/reports/votes_by_political_parties_distribution", methods=['GET'])
def get_political_parties_distribution():
    response = report_controller.get_votes_by_political_parties_distribution()
    return response, 200
