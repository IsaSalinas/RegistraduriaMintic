
class CandidateController:
    # constructor
    def __init__(self):
        """
        Constructor of the CandidateController class
        """
        print("Candidate controller ready...")

    def index(self) -> list:
        """
        This method gets all the candidates into the DB
        :return: Candidate's list
        """
        print("Get all")

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        print("Show by id")

    def create(self, candidate_: dict) -> dict:
        """
        :param candidate_:
        :return:
        """

        print("Insert")

    def update(self, id_: str, candidate_: dict) -> dict:
        """

        :param id_:
        :param candidate_:
        :return:
        """
        print("Update by id")

    def delete (self, id_: str ,) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete by id")
