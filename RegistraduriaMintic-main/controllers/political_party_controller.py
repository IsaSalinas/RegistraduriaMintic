class PoliticalPartyController:
    # constructor
    def __init__(self):
        """
        Constructor of the PoliticalPartyController class
        """
        print("Political party controller ready...")

    def index(self) -> list:
        """
        This method gets all the political parties into the DB
        :return: Political party's list
        """
        print("Get all")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")

    def create(self, political_party_: dict) -> dict:
        """

        :param political_party_:
        :return:
        """

        print("Insert")

    def update(self, id_: str, political_party_: dict) -> dict:
        """

        :param id_:
        :param political_party_:
        :return:
        """
        print("Update by id")

    def delete(self, id_: str, ) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete by id")
