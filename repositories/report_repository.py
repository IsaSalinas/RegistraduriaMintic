from bson import ObjectId

from repositories.interface_repository import InterfaceRepository
from models.vote import Vote


class ReportRepository(InterfaceRepository[Vote]):
    def get_votes_by_total_candidates(self):
        """
        It shows the greatest vote, for all candidate
        :return:
        """
        query_lookup = {
            "$lookup": {
                "from": "$candidate",
                "localField": "candidate.$id",
                "foreignField": "_id",
                "as": "details"
            }
        }
        query_unwind = {
            "$unwind": "details"
        }
        query_group = {
            "$group": {
                "_id": "$details",
                "count": {"$sum": 1}
            }
        }
        query_add_fields = {
            "$addFields": {
                "political_party": "$_id.political_party"
            }

        }
        query_sort = {
            "$sort": {
                "count": -1
            }
        }
        query_limit = {
            "$limit": 15
        }
        pipeline = [query_lookup, query_unwind, query_group, query_sort, query_limit]
        return self.query_aggregation(pipeline)

    def get_votes_by_candidate(self):
        """
        It shows the greatest vote, for all candidate
        :return:
        """
        query_match = {
            "$match": {
                "candidate.$id": ObjectId("$_id.candidate")
            }
        }
        query_lookup = {
            "$lookup": {
                "from": "$candidate",
                "localField": "candidate.$id",
                "foreignField": "_id",
                "as": "details"
            }
        }
        query_unwind = {
            "$unwind": "details"
        }
        query_group = {
            "$group": {
                "_id": "$details",
                "count": {"$sum": 1}
            }
        }
        query_add_fields = {
            "$addFields": {
                "political_party": "$_id.political_party"
            }
        }
        query_sort = {
            "$sort": {
                "count": -1
            }
        }
        pipeline = [query_match, query_lookup, query_unwind, query_group, query_add_fields, query_sort]
        return self.query_aggregation(pipeline)


    def get_votes_by_total_political_parties(self):
        """
        It shows the greatest vote, filtering by political party
        :return:
        """
        query_lookup = {
            "$lookup": {
                "from": "$political_party",
                "localField": "political_party.$id",
                "foreignField": "_id",
                "as": "details"
            }
        }
        query_unwind = {
            "$unwind": "details"
        }
        query_group = {
            "$group": {
                "_id": "$details",
                "count": {"$sum": 1}
            }
        }
        query_add_fields = {
            "$addFields": {
                "table": "$_id.table"
            }
        }
        query_sort = {
            "$sort": {
                "count": -1
            }
        }

        pipeline = [query_lookup, query_unwind, query_group, query_add_fields, query_sort]
        return self.query_aggregation(pipeline)


    def get_votes_by_total_tables(self):
            """
            It shows the greatest vote, filtering by table
            :return:
            """
            query_lookup = {
                "$lookup": {
                    "from": "$table",
                    "localField": "table.$id",
                    "foreignField": "_id",
                    "as": "details"
                }
            }
            query_unwind = {
                "$unwind": "details"
            }
            query_group = {
                "$group": {
                    "_id": "$details",
                    "count": {"$sum": 1}
                }
            }

            query_sort = {
                "$sort": {
                    "count": -1
                }
            }

            pipeline = [query_lookup, query_unwind, query_group, query_sort]
            return self.query_aggregation(pipeline)

    def get_votes_by_table(self):
            """
            It shows the greatest vote, filtering by table
            :return:
            """
            query_match = {
                "$match": {
                    "table.$id": ObjectId("$_id")
                }
            }
            query_lookup = {
                "$lookup": {
                    "from": "$table",
                    "localField": "table.$id",
                    "foreignField": "_id",
                    "as": "details"
                }
            }
            query_unwind = {
                "$unwind": "details"
            }
            query_group = {
                "$group": {
                    "_id": "$details",
                    "count": {"$sum": 1}
                }
            }

            query_sort = {
                "$sort": {
                    "count": -1
                }
            }

            pipeline = [query_match, query_lookup, query_unwind, query_group, query_sort]
            return self.query_aggregation(pipeline)
