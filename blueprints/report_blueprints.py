from flask import Blueprint
from controllers.report_controller import ReportController

report_blueprints = Blueprint('report_blueprints', __name__)
report_controller = ReportController()


@report_blueprints.route("/reports/highest_vote_by_candidate", methods=['GET'])
def get_highest_vote_by_candidate():
    response = report_controller.get_greatest_vote_by_candidate()
    return response, 200


@report_blueprints.route("/reports/highest_vote_by_political_party", methods=['GET'])
def get_highest_vote_by_political_party():
    response = report_controller.get_greatest_vote_by_political_party()
    return response, 200


@report_blueprints.route("/reports/highest_vote_by_table", methods=['GET'])
def get_highest_vote_by_table():
    response = report_controller.get_greatest_vote_by_table()
    return response, 200
