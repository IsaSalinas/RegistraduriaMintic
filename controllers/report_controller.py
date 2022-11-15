from repositories.report_repository import ReportRepository


class ReportController:
    def __init__(self):
        self.report_repository = ReportRepository()

    def get_greatest_vote_by_candidate(self):
        return self.report_repository.get_greatest_vote_by_candidate()

    def get_greatest_vote_by_political_party(self):
        return self.report_repository.get_greatest_vote_by_political_party()

    def get_greatest_vote_by_table(self):
        return self.report_repository.get_greatest_vote_by_table()
