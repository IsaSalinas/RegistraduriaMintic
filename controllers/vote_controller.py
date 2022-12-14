from models.vote import Vote
from repositories.vote_repository import VoteRepository
from models.table import Table
from models.candidate import Candidate
from repositories.table_repository import TableRepository
from repositories.candidate_repository import CandidateRepository


class VoteController:
    def __init__(self):
        """
        Constructor of the VoteController class
        """
        self.vote_repository = VoteRepository()
        self.table_repository = TableRepository()
        self.candidate_repository = CandidateRepository()

    def index(self) -> list:
        """
        This method gets all the votes into the DB
        :return: Vote's list
        """

        return self.vote_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.vote_repository.find_by_id(id_)

    def get_by_candidate(self, candidate_id: str) -> list:
        """

        :param candidate_id:
        :return:
        """
        return self.vote_repository.get_votes_in_candidate(candidate_id)

    def get_by_political_party(self, political_party_id: str) -> list:
        """

        :param political_party_id:
        :return:
        """
        return self.vote_repository.get_votes_in_political_party(political_party_id)

    def get_by_table(self, table_id: str) -> list:
        """

        :param table_id:
        :return:
        """
        return self.vote_repository.get_votes_in_table(table_id)

    def create(self, vote_: dict, candidate_id: str, table_id: str) -> dict:
        """

        :param table_id:
        :param candidate_id:
        :param vote_:
        :return:
        """
        vote = Vote(vote_)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        vote.candidate = candidate_obj
        vote.table = table_obj
        return self.vote_repository.save(vote)

    def update(self, id_: str, vote_: dict) -> dict:
        """

        :param id_:
        :param vote_:
        :return:
        """
        vote = Vote(vote_)
        return self.vote_repository.update(id_, vote)

    def delete(self, id_: str,) -> dict:
        """

        :param id_:
        :return:
        """
        return self.vote_repository.delete(id_)
