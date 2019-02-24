from paprika.repositories.Repository import Repository
from paprika_connector.connectors.Helper import Helper


class QueueRepository(Repository):
    def __init__(self, connector):
        Repository.__init__(self, connector)

    def list_active(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("select * from queues where active = 1")

        return Helper.cursor_to_json(cursor)

    def list(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("select * from queues")

        return Helper.cursor_to_json(cursor)

    def find_by_name(self, name):
        connection = self.get_connection()
        cursor = connection.cursor()

        param = dict()
        param['name'] = name

        statement = "select * from queues where name = :name"
        statement, parameters = self.statement(statement, param)

        cursor.execute(statement, parameters)
        result = Helper.cursor_to_json(cursor)

        if len(result) == 0:
            return None
        return result[0]
