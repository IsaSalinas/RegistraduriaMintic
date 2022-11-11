from flask import Blueprint
from controllers.report_controller import ReportController

report_blueprints = Blueprint('report_blueprints', __name__)
report_controller = ReportController()


@report_blueprints.route("/reports/highest_vote", methods=['GET'])
def get_highest_vote():
    response = report_controller.get_greatest_vote()
    return response, 200
