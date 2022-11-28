from repositories.report_repository import ReportRepository


class ReportController:
    def __init__(self):
        self.report_repository = ReportRepository()

    def get_votes_by_candidate(self):
        return self.report_repository.get_votes_by_candidate()

    def get_votes_by_total_candidates(self):
        return self.report_repository.get_votes_by_total_candidates()

    def get_votes_by_political_party(self):
        return self.report_repository.get_votes_by_political_party()

    def get_votes_by_political_parties_distribution(self):
        return self.report_repository.get_political_parties_distribution()

    def get_votes_by_total_tables(self):
        return self.report_repository.get_votes_by_total_tables()

    def get_votes_by_table(self):
        return self.report_repository.get_votes_by_table()
