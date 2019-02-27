# Ben Wasserman
# 02/25/19
# Database Management
# 2280906


class SQL:

    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def get_cursor(self):
        return self.cursor

    def execute_statement(self, statement, value_tuple):
        self.cursor.execute(statement, value_tuple)
        print(self.cursor.fetchall())

    def execute_full_statement(self, statement):
        self.cursor.execute(statement)
        print(self.cursor.fetchall())
