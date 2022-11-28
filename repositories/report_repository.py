from bson import ObjectId

from repositories.interface_repository import InterfaceRepository
from models.vote import Vote


class ReportRepository(InterfaceRepository[Vote]):
    def get_votes_by_total_candidates(self, id_: str = "-1", limit: int = None):
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
        query_limit = {}
        if limit:
            query_limit = {
                "$limit": limit
            }
        pipeline = [query_lookup, query_unwind, query_group, query_add_fields, query_sort, query_limit]
        return self.query_aggregation(pipeline)

    def get_votes_by_candidate(self, id_: str = "-1", limit: int = None):
        """
        It shows the greatest vote, for all candidate
        :return:
        """
        query_match = {"$match": {}}
        if id_ != "-1":
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
        query_limit = {}
        if limit:
            query_limit = {
                "$limit": limit
            }
        pipeline = [query_match, query_lookup, query_unwind, query_group, query_add_fields, query_sort, query_limit]
        return self.query_aggregation(pipeline)


    def get_votes_by_political_party(self):
        """
        It shows the greatest vote, filtering by political party
        :return:
        """
        query_preprocess_candidates = {
            "$lookup": {
                "from": "candidate",
                "localField": "candidate.$id",
                "foreignField": "_id",
                "as": "details"
            },
        }
        query_unwind_candidates = {
            "$unwind": "$details"
        }
        query_group_candidates = {
            "$group": {
                "_id": "$details",
                "count": {"$sum": 1}
            }
        }
        query_add_fields_political_party = {
            "$addFields": {
                "political_party": "$_id.political_party"
            }
        }
        query_process_political_parties = {
            "$lookup": {
                "from": "political_party",
                "localField": "political_party.$id",
                "foreignField": "_id",
                "as": "detailsP"
            }
        }
        query_unwind_political_party = {
            "$unwind": "$detailsP"
        }
        query_group_political_parties = {
            "$group": {
                "_id": "$detailsP",
                "enrollments": {"$sum": "$count"}
            },
        }
        query_add_fields = {
            "$addFields": {
                "name": "$_id.name",
                "_id": "$_id._id"
            }
        }
        pipeline = [query_preprocess_candidates, query_unwind_candidates, query_group_candidates, query_add_fields_political_party, query_process_political_parties,
                    query_unwind_political_party, query_group_political_parties, query_add_fields]
        return self.query_aggregation(pipeline)


    def get_votes_by_total_tables(self, id_: str = "-1", limit: int = None) -> list:
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
            query_add_fields = {
                "$addFields": {
                    "candidate": "$_id.candidate",
                    "political_party": "$_id.political_party"
                }
            }
            query_sort = {
                "$sort": {
                    "count": -1
                }
            }
            query_limit = {}
            if limit:
                query_limit = {
                    "$limit": limit
                }
            pipeline = [query_lookup, query_unwind, query_group, query_add_fields, query_sort, query_limit]
            return self.query_aggregation(pipeline)

    def get_votes_by_table(self, id_: str = "-1", limit: int = None) -> list:
            """
            It shows the greatest vote, filtering by table
            :return:
            """
            query_match = {"$match": {}}
            if id_ != "-1":
                query_match = {
                    "$match": {
                        "table.$id": ObjectId("$_id.table")
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
            query_add_fields = {
                "$addFields": {
                    "candidate": "$_id.candidate",
                    "political_party": "$_id.political_party"
                }
            }
            query_sort = {
                "$sort": {
                    "count": -1
                }
            }
            query_limit = {}
            if limit:
                query_limit = {
                    "$limit": limit
                }
            pipeline = [query_match, query_lookup, query_unwind, query_group, query_add_fields, query_sort, query_limit]
            return self.query_aggregation(pipeline)

    def get_political_parties_distribution(self) -> list:
        """
        :return:
        """
        winners = 15
        query_preprocess_candidates = {
            "$lookup": {
                "from": "candidate",
                "localField": "candidate.$id",
                "foreignField": "_id",
                "as": "details"
            },
            "$unwind": "$details"
        }
        query_group_candidates = {
            "$group": {
                "_id": "$details",
                "count": {"$sum": 1}
            },
            "$sort": {
                "count": -1
            },
            "$limit": winners,
            "$addFields": {
                "political_party": "$_id.political_party"
            }
        }
        query_preprocess_political_parties = {
            "$lookup": {
                "from": "political_party",
                "localField": "political_party.$id",
                "foreignField": "_id",
                "as": "detailsP"
            },
            "$unwind": "$detailsP"
        }
        query_group_political_parties = {
            "$group": {
                "_id": "$detailsP",
                "votes": {"$sum": "$count"}
            },
            "$addFields": {
                "name": "$_id.name",
                "_id": "$_id._id"
            }
        }
        pipeline = [query_preprocess_candidates, query_group_candidates, query_preprocess_political_parties,
                    query_group_political_parties]
        return self.query_aggregation(pipeline)