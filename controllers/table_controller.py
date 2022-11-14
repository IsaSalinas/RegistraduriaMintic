from models.table import Table
from repositories.table_repository import TableRepository

class TableController:
    def __init__(self):
        """
        Constructor of the TableController class
        """
        self.table_repository = TableRepository()

    def index(self) -> list:
        """
        This method gets all the tables into the DB
        :return: Table's list
        """
        return self.table_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        return self.table_repository.find_by_id(id_)

    def create(self, table_: dict) -> dict:
        """
        :param table_:
        :return:
        """

        table = Table(table_)
        return self.table_repository.save(table)

    def update(self, id_: str, table_: dict) -> dict:
        """
        :param id_:
        :param table_:
        :return:
        """
        table = Table(table_)
        return self.table_repository.update(id_, table)

    def delete(self, id_: str, ) -> str:
        """
        :param id_:
        :return:
        """
        return self.table_repository.delete(id_)

