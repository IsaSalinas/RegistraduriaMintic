from repositories.interface_repository import InterfaceRepository
from models.vote import Vote


class ReportRepository(InterfaceRepository[Vote]):
    def get_greatest_vote(self):
        query_aggregation = {
                "_id": "$candidate",
                "max": {"$max": "$vote"},
                "doc": {"first": "$$ROOT"}
            }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)
