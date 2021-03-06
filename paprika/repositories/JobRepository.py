from paprika.repositories.Repository import Repository


class JobRepository(Repository):
    def __init__(self, connector):
        Repository.__init__(self, connector)

    def insert(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        statement = "insert into jobs() values ()"

        cursor.execute(statement)

        message=dict()
        message['id'] = cursor.lastrowid

        connection.commit()

        return message

    def job(self):
        message = self.insert()
        message['job_name'] = 'JOB$_' + str(message['id'])

        return message
