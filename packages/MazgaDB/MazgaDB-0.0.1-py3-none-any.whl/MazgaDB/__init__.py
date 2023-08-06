import sqlite3
from prettytable import from_db_cursor


class MazgaDB:
    def __init__(self, db: str, data_classes: dict = dict()):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.db = db
        self.data_class = data_classes

    def accept_columns(self, name_table: str):
      self.cur.execute("SELECT * FROM sqlite_master")
      
      for tables in self.cur.fetchall():
        if name_table in tables:
          break
      else:
        raise ValueError('no such table exists')
        
      columns = [
            column.split()[0]
            for column in tables[-1].split("(")[1].replace(")", "").split(",")
      ]
              
      return columns


    

    def create_table(self, name_table: str, param: dict):
        """Пример создания таблицы CREATE TABLE IF NOT EXISTS users(
        userid INT PRIMARY KEY,
        fname TEXT,
        lname TEXT,
        gender TEXT);
        """
        self.execute(
            f"""CREATE TABLE IF NOT EXISTS {name_table}({','.join([t + ' ' + param[t] for t in param])});"""
        )

    def append_line(self, name_table: str, values: list):
        self.execute(
            f"""INSERT INTO {name_table} VALUES({','.join(['"' + str(t) + '"' for t in values])});"""
        )

    def update_line(
        self, name_table: str, key1: str, value1: str, key2: str, value2: str
    ):
        self.execute(
            f"UPDATE {name_table} SET {key2} = '{value2}' WHERE {key1} = '{value1}' "
        )

    def delete_line(self, name_table: str, key: str, value: str):
        self.execute(f"""DELETE from {name_table} where {key} = {value}""")

    def append_column(self, name_table: str, name_column: str, type_column: str):
        self.execute(
            f"alter table {name_table} add column {name_column} '{type_column}'"
        )

    def delete_column(self, name_table: str, column: str):
        """
        Передайте те столбцы которые хотите оставить
        """

        columns = self.accept_columns(name_table)

        columns.remove(column)

        self.execute(
            f"CREATE TABLE config AS SELECT {','.join(columns)} FROM {name_table};"
        )
        self.execute(f"DROP TABLE {name_table}")
        self.execute(f"ALTER TABLE config RENAME TO {name_table};")

    def is_there(self, name_table: str, key: str, value: str) -> bool:
        self.cur.execute(f"SELECT * FROM {name_table} WHERE {key} = {value}")
        return True if len(self.cur.fetchall()) > 0 else False

    def read_table(self, name_table: str, type: str = 's', param: list = None) -> str:
        try:
            self.cur.execute(
                f"SELECT {','.join(param) if param else '*'} FROM {name_table}"
            )
            mytable = from_db_cursor(self.cur)

            if type == 's':
              return str(mytable)
            elif type == 'm':
              counts = len(self.accept_columns(name_table)) + 1
              
              table = str(mytable).replace('+','-', counts).replace('+','|', counts).replace('+','-')
              return table

            else:
              raise ValueError('unknown type')
            
        except sqlite3.Error as error:
            return error

    def saw_tables(self):
        """
        Возращает все таблицы из базы данных
        """
        return self.execute("SELECT name FROM sqlite_master WHERE type='table';")

    def select_class(
        self, name_table: str, key, value, param: str = "*", class_data=None
    ):
        self.cur.execute(f"SELECT {param} FROM {name_table} WHERE {key} = {value}")
        if class_data:
            return class_data(*self.cur.fetchall()[0])
        elif name_table in self.data_class:
            return self.data_class[name_table](*self.cur.fetchall()[0])
        else:
            return None
    def select(self, name_table: str, key, value, param: str = "*"):
        """
        Обычный SELECT из SQL
        """
        self.cur.execute(f"SELECT {param} FROM {name_table} WHERE {key} = {value}")
        return self.cur.fetchall()

    def execute(self, sql_request: str, params: list = None):
        self.cur.execute(sql_request)
        self.conn.commit()
        return self.cur.fetchall()