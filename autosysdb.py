from datetime import datetime
from sqlite4 import SQLite4

database = SQLite4('db/autosys.db')
database.connect()
database.create_table('test', ['job_name', 'status', 'datetime'])
database.insert('test', {'job_name': 'My_Test_AUTOSYS_Job1', 'status': 1, 'datetime': datetime.now()})
database.disconnect()