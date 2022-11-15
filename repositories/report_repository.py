from repositories.interface_repository import InterfaceRepository
from models.vote import Vote


class ReportRepository(InterfaceRepository[Vote]):
    def get_greatest_vote_by_candidate(self):
        """
        It shows the greatest vote, filtering by candidate
        :return:
        """
        query_aggregation = {
                "_id": "$candidate",
                "max": {"$max": "$vote"},
                "doc": {"first": "$$ROOT"}
            }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)

    def get_greatest_vote_by_political_party(self):
        """
        It shows the greatest vote, filtering by political party
        :return:
        """
        query_aggregation = {
                "_id": "$political_party",
                "max": {"$max": "$vote"},
                "doc": {"first": "$$ROOT"}
            }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)

    def get_greatest_vote_by_table(self):
        """
        It shows the greatest vote, filtering by political party
        :return:
        """
        query_aggregation = {
            "_id": "$table",
            "max": {"$max": "$vote"},
            "doc": {"first": "$$ROOT"}
        }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)
