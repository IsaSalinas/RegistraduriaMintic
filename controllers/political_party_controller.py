from models.political_party import PoliticalParty
from repositories.political_party_repository import PoliticalPartyRepository


class PoliticalPartyController:
    # constructor
    def __init__(self):
        """
        Constructor of the PoliticalPartyController class
        """
        print("Political party controller ready...")
        self.political_party_repository = PoliticalPartyRepository()

    def index(self) -> list:
        """
        This method gets all the political parties into the DB
        :return: Political party's list
        """
        print("Get all")
        return self.political_party_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        print("Show by id")
        return self.political_party_repository.find_by_id(id_)

    def create(self, political_party_: dict) -> dict:
        """
        :param political_party_:
        :return:
        """

        print("Insert")
        political_party_ = PoliticalParty(political_party_)
        return self.political_party_repository.save(political_party_)

    def update(self, id_: str, political_party_: dict) -> dict:
        """
        :param id_:
        :param political_party_:
        :return:
        """
        print("Update by id")
        political_party = PoliticalParty(political_party_)
        return self.political_party_repository.update(id_, political_party)

    def delete(self, id_: str, ) -> str:
        """
        :param id_:
        :return:
        """
        print("Delete by id")
        return self.political_party_repository.delete(id_)