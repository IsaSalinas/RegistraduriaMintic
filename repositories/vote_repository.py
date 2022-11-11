from bson import ObjectId

from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class VoteRepository(InterfaceRepository[Vote]):
    #Verificar parametros
    def get_votes_in_table(self, table_id: str) -> list:
        """

        :param table_id:
        :return:
        """
        query = {"table.$id": ObjectId(table_id)}
        return self.query(query)

    def get_votes_in_candidate(self, candidate_id: str) -> list:
        """

        :param candidate_id:
        :return:
        """
        query = {"candidate.$id": ObjectId(candidate_id)}
        return self.query(query)

    def get_votes_in_political_party(self, political_party_id: str) -> list:
        """

        :param political_party_id:
        :return:
        """
        query = {"political_party.$id": ObjectId(political_party_id)}
        return self.query(query)
