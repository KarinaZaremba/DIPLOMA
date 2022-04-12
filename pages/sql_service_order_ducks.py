
class SqlService:
    def __init__(self, connection):
        self.connection = connection

    def execute_sql_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    def get_id_of_order(self):
        numbers_of_orders = self.execute_sql_query("SELECT id FROM lc_orders")
        return numbers_of_orders
