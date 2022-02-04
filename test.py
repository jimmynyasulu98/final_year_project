import database
from datetime import datetime
if __name__ == "__main__":
    con = database.connect()
    database.create_tables(con)
    database.insert_update(con, 'door', 'opened', datetime.now())
    print(database.get_all_updates(con))
