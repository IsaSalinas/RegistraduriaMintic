from models.candidate import Candidate
from models.political_party import PoliticalParty
from repositories.candidate_repository import CandidateRepository
from repositories.political_party_repository import PoliticalParty

class CandidateController:
    # constructor
    def __init__(self):
        """
        Constructor of the CandidateController class
        """
        print("Candidate controller ready...")
        self.candidate_repository = CandidateRepository()

    def index(self) -> list:
        """
        This method gets all the candidates into the DB
        :return: Candidate's list
        """
        print("Get all")
        return self.candidate_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.candidate_repository.find_by_id(id_)

    def create(self, candidate_: dict) -> dict:
        """

        :param candidate_:
        :return:
        """

        print("Insert")
        candidate = Candidate(candidate_)

        return self.candidate_repository.save(candidate)

    def update(self, id_: str, candidate_: dict) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("Update by id")
        candidate = Candidate(candidate_)
        return self.candidate_repository.update(id_, candidate)

    def delete (self, id_: str ,) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete by id")
        return self.candidate_repository.delete(id_)

    def political_party_assign(self, candidate_id: str, political_party_id: str) -> dict:
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidate(candidate_dict)
        political_party_dict = self.political_party_repository.find_by_id(political_party_id)

        political_party_obj = PoliticalParty(political_party_dict)
        candidate_obj.department = political_party_obj
        return self.candidate_repository.save(candidate_obj)