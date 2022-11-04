class TableController:
    # constructor
    def __init__(self):
        """
        Constructor of the TableController class
        """
        print("Table controller ready...")

    def index(self) -> list:
        """
        This method gets all the tables into the DB
        :return: Table's list
        """
        print("Get all")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")

    def create(self, table_: dict) -> dict:
        """

        :param table_:
        :return:
        """

        print("Insert")

    def update(self, id_: str, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("Update by id")

    def delete(self, id_: str, ) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete by id")
