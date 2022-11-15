from models.candidate import Candidate
from repositories.candidate_repository import CandidateRepository
from models.political_party import PoliticalParty
from repositories.political_party_repository import PoliticalPartyRepository


class CandidateController:
    def __init__(self):
        """
        Constructor of the CandidateController class
        """
        self.candidate_repository = CandidateRepository()
        self.political_party_repository = PoliticalPartyRepository()

    def index(self) -> list:
        """
        This method gets all the candidates into the DB
        :return: Candidate's list
        """
        return self.candidate_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        return self.candidate_repository.find_by_id(id_)

    def create(self, candidate_: dict) -> dict:
        """
        :param candidate_:
        :return:
        """
        candidate = Candidate(candidate_)
        return self.candidate_repository.save(candidate)

    def update(self, id_: str, candidate_: dict) -> dict:
        """
        :param id_:
        :param candidate_:
        :return:
        """
        candidate = Candidate(candidate_)
        return self.candidate_repository.update(id_, candidate)

    def delete (self, id_: str ,) -> dict:
        """
        :param id_:
        :return:
        """
        return self.candidate_repository.delete(id_)

    def political_party_assign(self, candidate_id: str, political_party_id: str) -> dict:
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        political_party_dict = self.political_party_repository.find_by_id(political_party_id)
        political_party_obj = PoliticalParty(political_party_dict)
        candidate_obj.political_party = political_party_obj
        return self.candidate_repository.save(candidate_obj)